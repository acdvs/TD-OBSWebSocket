import json

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

	if msg['op'] == 0:
		parent().Identify(data)
	elif msg['op'] == 2:
		parent().par.Connected = True
	elif msg['op'] == 5:
		parent().HandleEvent(data)