import json
import re
from typing import Tuple, cast
import urllib.request

Version = Tuple[int, int, int]

schema = None
schemaUrl = "https://raw.githubusercontent.com/obsproject/obs-websocket/master/docs/generated/protocol.json"

with urllib.request.urlopen(schemaUrl) as res:
    schema = json.load(res)


def buildEventPars(wsVersion: str = None):
    events = schema["events"]

    for event in events:
        if wsVersion and not wsVersionHasEvent(wsVersion, event["initialVersion"]):
            continue

        page = createOrGetPage(event["category"])
        parName = eventTypeToName(event["eventType"])
        parLabel = labelize(event["eventType"])

        if len(event["dataFields"]) == 0:
            par = page.appendPulse(parName, label=parLabel)
        else:
            par = page.appendPython(parName, label=parLabel)

        par.help = event["description"]
        par.readOnly = True


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


def wsVersionHasEvent(wsVersion: str, eventVersion: str):
    wsVersions = parseVersionString(wsVersion)
    eventVersions = parseVersionString(eventVersion)

    if (
        wsVersions[0] < eventVersions[0]
        or wsVersions[1] < eventVersions[1]
        or wsVersions[2] < eventVersions[2]
    ):
        return False

    return True


def parseVersionString(version: str):
    parsed = version.split(".")
    return cast(Version, parsed)
