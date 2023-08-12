import json
from OBSEnums import WebSocketOpCode, RequestStatus

# me - this DAT
# dat - the DAT that received a message
# rowIndex - the row number the message was placed into
# message - a unicode representation of the text
# 
# Only text frame messages will be handled in this function.

def onDisconnect(dat):
	parent().par.Connected = False

def onReceiveText(dat, rowIndex, message):
	msg = json.loads(message)
	data = msg['d']
	opCode = msg['op']

	if opCode == WebSocketOpCode.HELLO:
		parent().Identify(data)
	elif opCode == WebSocketOpCode.IDENTIFIED:
		parent().par.Connected = True
	elif opCode == WebSocketOpCode.EVENT:
		parent().HandleEvent(data)
	elif opCode == WebSocketOpCode.REQUEST_RESPONSE:
		op('request_responses').clear(keepFirstRow=True)
		handleResponse(data)
	elif opCode == WebSocketOpCode.REQUEST_BATCH_RESPONSE:
		op('request_responses').clear(keepFirstRow=True)

		for res in data['results']:
			handleResponse(res)

def handleResponse(data):
	status = data['requestStatus']
	typ = data['requestType']
	requestId = data['requestId'] if 'requestId' in data else ''

	if status['result'] == True:
		op('request_responses').appendRow([typ, requestId, data['responseData']])
	else:
		parent().addScriptError(f"Bad OBS request\nCode: {RequestStatus(status['code']).name}\nType: {typ}\nComment: {status['comment']}")