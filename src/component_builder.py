from packaging.version import Version
import re

from obs_schema import Event, loadSchema


def buildEventPars(ws_version: Version = None):
    schema = loadSchema()
    events: list[Event] = schema["events"]

    for event in events:
        page = createOrGetPage(event["category"])
        par_name = eventTypeToName(event["eventType"])
        par_label = labelize(event["eventType"])

        if len(event["dataFields"]) == 0:
            par = page.appendPulse(par_name, label=par_label)
        else:
            par = page.appendPython(par_name, label=par_label)

        par.help = event["description"]
        par.readOnly = True

        if ws_version and ws_version < Version(event["initialVersion"]):
            par.enable = False
            par.help = (
                "EVENT NOT SUPPORTED IN ACTIVE OBS WEBSOCKET VERSION\n\n" + par.help
            )


def createOrGetPage(cat_name: str):
    parent_op = parent().asType(baseCOMP)

    page_name = labelize(cat_name.capitalize())
    pages = parent_op.customPages
    page = next((page for page in pages if page == page_name), None)

    if not page:
        page = parent_op.appendCustomPage(page_name)

    return page


def labelize(text: str):
    label = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)

    if label == "Ui":
        return "UI"

    return label


def eventTypeToName(event_type: str):
    return event_type.lower().capitalize()
