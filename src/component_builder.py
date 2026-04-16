import json
import re
import urllib.request

url = 'https://raw.githubusercontent.com/obsproject/obs-websocket/master/docs/generated/protocol.json'

def buildEventPars():
    with urllib.request.urlopen(url) as res:
        data = json.load(res)

    wsVersion = parseVersionString(parent().RecentWsVersion)
    events = data['events']

    for event in events:
        eventVersion = parseVersionString(event['initialVersion'])

        if not wsVersionHasEvent(wsVersion, eventVersion):
            continue

        page = createOrGetPage(event['category'])
        parName = eventTypeToName(event['eventType'])
        parLabel = labelize(event['eventType'])

        if len(event['dataFields']) == 0:
            par = page.appendPulse(parName, label=parLabel)
        else:
            par = page.appendPython(parName, label=parLabel)
        
        par.help = event['description']
        par.readOnly = True

def createOrGetPage(catName):
    pageName = labelize(catName.capitalize())
    pages = parent().customPages
    page = next((page for page in pages if page == pageName), None)

    if not page:
        page = parent().appendCustomPage(pageName)
    
    return page

def labelize(text):
    label = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    
    if label == 'Ui':
        return 'UI'
    
    return label

def eventTypeToName(eventType):
    return eventType.lower().capitalize()

def wsVersionHasEvent(wsVersion, eventVersion):
    if (wsVersion[0] < eventVersion[0] or
        wsVersion[1] < eventVersion[1] or
        wsVersion[2] < eventVersion[2]):
        return False
    
    return True

def parseVersionString(version):
    return version.split('.')