import webbrowser

# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
# 
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.

def onValueChange(par, val, prev):
	if (par.name == 'Includeinputvolumemeters' or
			par.name == 'Includeinputactivestatechanged' or
			par.name == 'Includeinputshowstatechanged' or
			par.name == 'Includesceneitemtransformchanged'):
		parent().Reidentify()

def onPulse(par):
	if par.name == 'Opendocumentation':
		url = 'https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md'
		webbrowser.open_new_tab(url)