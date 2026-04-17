import json

from obs_enums import WebSocketOpCode, RequestStatus


def onDisconnect(dat):
    parent().par.Connected = False


def onReceiveText(dat, rowIndex, message: str):
    msg = json.loads(message)
    data = msg["d"]
    opCode = msg["op"]

    if opCode == WebSocketOpCode.HELLO:
        parent().Identify(data)
    elif opCode == WebSocketOpCode.IDENTIFIED:
        parent().par.Connected = True
    elif opCode == WebSocketOpCode.EVENT:
        parent().HandleEvent(data)
    elif opCode == WebSocketOpCode.REQUEST_RESPONSE:
        op("responses").clear(keepFirstRow=True)
        handleResponse(data)
    elif opCode == WebSocketOpCode.REQUEST_BATCH_RESPONSE:
        op("responses").clear(keepFirstRow=True)

        for res in data["results"]:
            handleResponse(res)


def handleResponse(data):
    status = data["requestStatus"]
    requestType = data["requestType"]
    requestId = data["requestId"] if "requestId" in data else ""

    if status["result"]:
        op("responses").appendRow([requestType, requestId, data["responseData"]])
    else:
        requestStatus = RequestStatus(status["code"]).name
        message = "Bad OBS request\nCode: {}\nType: {}\nComment: {}".format(
            requestStatus, requestType, status["comment"]
        )
        parent().addScriptError(message)
