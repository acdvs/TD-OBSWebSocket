import json

from obs_enums import WebSocketOpCode, RequestStatus
from obs_schema import BaseMessage, RequestResponseMessage
from obs_websocket import OBSWebSocket


def onDisconnect(dat):
    parent().par.Connected = False


def onReceiveText(dat, rowIndex, message: str):
    parentOP = parent().asType(OBSWebSocket)
    responsesOP = op("responses").asType(tableDAT)

    msg: BaseMessage = json.loads(message)
    data = msg["d"]
    opCode = msg["op"]

    if opCode == WebSocketOpCode.HELLO:
        parentOP.Identify(data)
    elif opCode == WebSocketOpCode.IDENTIFIED:
        parentOP.par.Connected = True
    elif opCode == WebSocketOpCode.EVENT:
        parentOP.HandleEvent(data)
    elif opCode == WebSocketOpCode.REQUEST_RESPONSE:
        responsesOP.clear(keepFirstRow=True)
        handleResponse(data)
    elif opCode == WebSocketOpCode.REQUEST_BATCH_RESPONSE:
        responsesOP.clear(keepFirstRow=True)

        for res in data["results"]:
            handleResponse(res)


def handleResponse(data: RequestResponseMessage):
    responsesOP = op("responses").asType(tableDAT)

    status = data["requestStatus"]
    requestType = data["requestType"]
    requestId = data["requestId"] if "requestId" in data else ""
    responseData = data["responseData"] if "responseData" in data else ""

    if status["result"]:
        responsesOP.appendRow([requestType, requestId, responseData])
    else:
        requestStatus = RequestStatus(status["code"]).name
        message = "Bad OBS request\nCode: {}\nType: {}\nComment: {}".format(
            requestStatus, requestType, status["comment"]
        )
        responsesOP.addScriptError(message)
