import webbrowser

from component_builder import buildEventPars
from obs_websocket import OBSWebSocket


def onValueChange(par: Par):
    if (
        par.name == "Includeinputvolumemeters"
        or par.name == "Includeinputactivestatechanged"
        or par.name == "Includeinputshowstatechanged"
        or par.name == "Includesceneitemtransformchanged"
    ):
        parentOP = parent().asType(OBSWebSocket)
        parentOP.Reidentify()


def onPulse(par: Par):
    schemaUrl = parent().fetch("docs_url")

    if par.name == "Opendocumentation":
        webbrowser.open_new_tab(schemaUrl)
        return

    if par.name == "Updatepars":
        for page in parent().customPages:
            if page.index >= 1:
                page.destroy()

        buildEventPars()
