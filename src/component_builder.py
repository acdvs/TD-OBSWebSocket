from packaging.version import Version
import re
from typing import Tuple, cast
import urllib.request

schema = None
schemaUrl = "https://raw.githubusercontent.com/obsproject/obs-websocket/master/docs/generated/protocol.json"

with urllib.request.urlopen(schemaUrl) as res:
    schema = json.load(res)


def buildEventPars(wsVersion: Version = None):
    events = schema["events"]

    for event in events:
        page = createOrGetPage(event["category"])
        parName = eventTypeToName(event["eventType"])
        parLabel = labelize(event["eventType"])

        if len(event["dataFields"]) == 0:
            par = page.appendPulse(parName, label=parLabel)
        else:
            par = page.appendPython(parName, label=parLabel)

        par.help = event["description"]
        par.readOnly = True

        if wsVersion and wsVersion < Version(event["initialVersion"]):
            par.enable = False
            par.help = (
                "EVENT NOT SUPPORTED IN ACTIVE OBS WEBSOCKET VERSION\n\n" + par.help
            )


def createOrGetPage(catName: str):
    parentOP = parent().asType(baseCOMP)

    pageName = labelize(catName.capitalize())
    pages = parentOP.customPages
    page = next((page for page in pages if page == pageName), None)

    if not page:
        page = parentOP.appendCustomPage(pageName)

    return page


def labelize(text: str):
    label = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)

    if label == "Ui":
        return "UI"

    return label


def eventTypeToName(eventType: str):
    return eventType.lower().capitalize()
