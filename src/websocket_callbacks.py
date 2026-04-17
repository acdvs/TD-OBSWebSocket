import json

from obs_enums import WebSocketOpCode, RequestStatus
from obs_websocket import OBSWebSocket

module = parent().asType(OBSWebSocket)
responsesOP = op('request_responses').asType(tableDAT)

def onDisconnect(dat):
	parent().par.Connected = False

def onReceiveText(dat, rowIndex, message: str):
	msg = json.loads(message)
	data = msg['d']
	opCode = msg['op']

	if opCode == WebSocketOpCode.HELLO:
		module.Identify(data)
	elif opCode == WebSocketOpCode.IDENTIFIED:
		module.par.Connected = True
	elif opCode == WebSocketOpCode.EVENT:
		module.HandleEvent(data)
	elif opCode == WebSocketOpCode.REQUEST_RESPONSE:
		responsesOP.clear(keepFirstRow=True)
		handleResponse(data)
	elif opCode == WebSocketOpCode.REQUEST_BATCH_RESPONSE:
		responsesOP.clear(keepFirstRow=True)

		for res in data['results']:
			handleResponse(res)

def handleResponse(data):
	status = data['requestStatus']
	requestType = data['requestType']
	requestId = data['requestId'] if 'requestId' in data else ''

	if status['result']:
		responsesOP.appendRow([requestType, requestId, data['responseData']])
	else:
		message = "Bad OBS request\nCode: {}\nType: {}\nComment: {}".format(RequestStatus(status['code']).name, requestType, status['comment'])
		module.addScriptError(message)