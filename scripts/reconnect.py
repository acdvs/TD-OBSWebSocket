# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

def onValueChange(channel, sampleIndex, val, prev):
	if (not parent().par.Connected and
			parent().par.Autoreconnect and
			parent().par.Address != '' and
			parent().par.Port != ''):
		op('websocket').par.reset.pulse()