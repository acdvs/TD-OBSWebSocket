from base64 import b64encode
from collections import abc
from hashlib import sha256
import json
from packaging.version import Version
from uuid import uuid4

from component_builder import buildEventPars, eventTypeToName
from obs_enums import (
    WebSocketOpCode,
    EventSubscription,
    RequestType,
    RequestBatchExecutionType,
)
from obs_schema import EventMessage, HelloMessage


class OBSWebSocket:
    def __init__(self, parentOP: baseCOMP):
        self.parentOP = parentOP
        self.websocketOP = op("websocket").asType(websocketDAT)
        self.responsesOP = op("responses").asType(tableDAT)

        self.RequestType = RequestType
        self.RequestBatchExecutionType = RequestBatchExecutionType

        self.parentOP.par.Connected = False

        self.websocketOP.clear()
        self.responsesOP.clear(keepFirstRow=True)

    def Identify(self, data: HelloMessage):
        obsWebSocketVersion = Version(data["obsWebSocketVersion"])
        buildEventPars(obsWebSocketVersion)

        response = {
            "op": WebSocketOpCode.IDENTIFY,
            "d": {"rpcVersion": 1, "eventSubscriptions": self.getSubscriptionBitmask()},
        }

        if "authentication" in data:
            secret = self.toHashedBase64String(
                self.parentOP.par.Password + data["authentication"]["salt"]
            )
            auth = self.toHashedBase64String(
                secret + data["authentication"]["challenge"]
            )

            response["d"]["authentication"] = auth

        self.websocketOP.sendText(json.dumps(response))

    def toHashedBase64String(self, data: str):
        bytesData = data.encode()
        hashedData = sha256(bytesData).digest()
        base64Data = b64encode(hashedData)
        return base64Data.decode()

    def Reidentify(self):
        message = {"eventSubscriptions": self.getSubscriptionBitmask()}

        self.websocketOP.sendText(json.dumps(message))

    def getSubscriptionBitmask(self):
        bitmask = EventSubscription.ALL

        if self.parentOP.par.Includeinputvolumemeters:
            bitmask |= EventSubscription.INPUT_VOLUME_METERS
        if self.parentOP.par.Includeinputactivestatechanged:
            bitmask |= EventSubscription.INPUT_ACTIVE_STATE_CHANGED
        if self.parentOP.par.Includeinputshowstatechanged:
            bitmask |= EventSubscription.INPUT_SHOW_STATE_CHANGED
        if self.parentOP.par.Includesceneitemtransformchanged:
            bitmask |= EventSubscription.SCENE_ITEM_TRANSFORM_CHANGED

        return bitmask

    def SendRequest(self, typ, rid=str(uuid4()), data=None):
        self.parentOP.clearScriptErrors()

        if isinstance(typ, RequestType):
            typ = typ.value

        request = {
            "op": WebSocketOpCode.REQUEST,
            "d": {"requestType": typ, "requestId": rid, "requestData": data},
        }

        self.websocketOP.sendText(json.dumps(request))

    def SendRequestBatch(
        self,
        data,
        executionType=RequestBatchExecutionType.SERIAL_REALTIME,
        haltOnFailure=False,
    ):
        self.parentOP.clearScriptErrors()

        if isinstance(data, abc.Sequence):
            for request in data:
                if isinstance(request["requestType"], RequestType):
                    request["requestType"] = request["requestType"].value

        request = {
            "op": WebSocketOpCode.REQUEST_BATCH,
            "d": {
                "requestId": str(uuid4()),
                "haltOnFailure": haltOnFailure,
                "executionType": executionType,
                "requests": data,
            },
        }

        self.websocketOP.sendText(json.dumps(request))

    def HandleEvent(self, data: EventMessage):
        paramName = eventTypeToName(data["eventType"])

        if "eventData" in data:
            self.parentOP.par[paramName].val = data["eventData"]
        else:
            self.parentOP.par[paramName].pulse()
