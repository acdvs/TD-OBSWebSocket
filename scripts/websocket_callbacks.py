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
		parent().HandleEvent(data)		parent().HandleEvent(data)
