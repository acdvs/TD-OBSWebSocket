import json

from obs_enums import WebSocketOpCode
from obs_schema import BaseMessage, RequestResponseMessage
from obs_websocket import OBSWebSocket


def onDisconnect(dat):
    parent().par.Connected = False


def onReceiveText(dat, row_index, message: str):
    parent_op = parent().asType(OBSWebSocket)
    responses_op = op("responses").asType(tableDAT)

    msg: BaseMessage = json.loads(message)
    data = msg["d"]
    op_code = msg["op"]

    if op_code == WebSocketOpCode.HELLO:
        parent_op.Identify(data)
    elif op_code == WebSocketOpCode.IDENTIFIED:
        parent_op.par.Connected = True
    elif op_code == WebSocketOpCode.EVENT:
        parent_op.HandleEvent(data)
    elif op_code == WebSocketOpCode.REQUEST_RESPONSE:
        responses_op.clear(keepFirstRow=True)
        handle_response(data)
    elif op_code == WebSocketOpCode.REQUEST_BATCH_RESPONSE:
        responses_op.clear(keepFirstRow=True)

        for res in data["results"]:
            handle_response(res, data["requestId"])


def handle_response(data: RequestResponseMessage, batch_id: str = None):
    responses_op = op("responses").asType(tableDAT)

    status = data["requestStatus"]
    request_type = data["requestType"]
    request_id = data["requestId"] if "requestId" in data else ""
    batch_id = batch_id or ""

    row_data = data["responseData"] if "responseData" in data else "{}"

    responses_op.appendRow([request_type, row_data, status, request_id, batch_id])
