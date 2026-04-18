import json

from obs_enums import WebSocketOpCode, RequestStatus
from obs_schema import BaseMessage, RequestResponseMessage
from obs_websocket import OBSWebSocket


def onDisconnect(dat):
    parent().par.Connected = False


def onReceiveText(dat, row_index, message: str):
    parent_op = parent().asType(OBSWebSocket)
    responses_op = op("responses").asType(tableDAT)

    msg: BaseMessage = json.loads(message)
    data = msg["d"]
    opCode = msg["op"]

    if opCode == WebSocketOpCode.HELLO:
        parent_op.Identify(data)
    elif opCode == WebSocketOpCode.IDENTIFIED:
        parent_op.par.Connected = True
    elif opCode == WebSocketOpCode.EVENT:
        parent_op.HandleEvent(data)
    elif opCode == WebSocketOpCode.REQUEST_RESPONSE:
        responses_op.clear(keepFirstRow=True)
        handleResponse(data)
    elif opCode == WebSocketOpCode.REQUEST_BATCH_RESPONSE:
        responses_op.clear(keepFirstRow=True)

        for res in data["results"]:
            handleResponse(res)


def handleResponse(data: RequestResponseMessage):
    responses_op = op("responses").asType(tableDAT)

    status = data["requestStatus"]
    request_type = data["requestType"]
    request_id = data["requestId"] if "requestId" in data else ""
    response_data = data["responseData"] if "responseData" in data else ""

    if status["result"]:
        responses_op.appendRow([request_type, request_id, response_data])
    else:
        requestStatus = RequestStatus(status["code"]).name
        message = "Bad OBS request\nCode: {}\nType: {}\nComment: {}".format(
            requestStatus, request_type, status["comment"]
        )
        responses_op.addScriptError(message)
