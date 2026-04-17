import webbrowser

from component_builder import buildEventPars
from obs_websocket import OBSWebSocket

docsUrl = 'https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md'
module = parent().asType(OBSWebSocket)

def onValueChange(par: Par):
	if (par.name == 'Includeinputvolumemeters' or
			par.name == 'Includeinputactivestatechanged' or
			par.name == 'Includeinputshowstatechanged' or
			par.name == 'Includesceneitemtransformchanged'):
		module.Reidentify()

def onPulse(par: Par):
	if par.name == 'Opendocumentation':
		webbrowser.open_new_tab(docsUrl)
		return
	
	if par.name == 'Updatepars' and module.RecentWsVersion:		
		for page in parent().customPages:
			if page.index >= 1:
				page.destroy()
		
		buildEventPars(module.RecentWsVersion)
