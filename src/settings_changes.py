import webbrowser

from component_builder import build_event_pars
from obs_websocket import OBSWebSocket


def onValueChange(par: Par):
    if (
        par.name == "Includeinputvolumemeters"
        or par.name == "Includeinputactivestatechanged"
        or par.name == "Includeinputshowstatechanged"
        or par.name == "Includesceneitemtransformchanged"
    ):
        parent_op = parent().asType(OBSWebSocket)
        parent_op.Reidentify()


def onPulse(par: Par):
    schema_url = parent().fetch("docs_url")

    if par.name == "Opendocumentation":
        webbrowser.open_new_tab(schema_url)
        return

    if par.name == "Updatedata":
        for page in parent().customPages:
            if page.index >= 1:
                page.destroy()

        build_event_pars()
