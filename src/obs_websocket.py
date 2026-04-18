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
    def __init__(self, parent_op: baseCOMP):
        self.parent_op = parent_op
        self.websocket_op = op("websocket").asType(websocketDAT)
        self.responses_op = op("responses").asType(tableDAT)

        self.RequestType = RequestType
        self.RequestBatchExecutionType = RequestBatchExecutionType

        self.parent_op.par.Connected = False

        self.websocket_op.clear()
        self.responses_op.clear(keepFirstRow=True)

    def Identify(self, data: HelloMessage):
        obs_websocket_version = Version(data["obsWebSocketVersion"])
        buildEventPars(obs_websocket_version)

        response = {
            "op": WebSocketOpCode.IDENTIFY,
            "d": {"rpcVersion": 1, "eventSubscriptions": self.getSubscriptionBitmask()},
        }

        if "authentication" in data:
            secret = self.toHashedBase64String(
                self.parent_op.par.Password + data["authentication"]["salt"]
            )
            auth = self.toHashedBase64String(
                secret + data["authentication"]["challenge"]
            )

            response["d"]["authentication"] = auth

        self.websocket_op.sendText(json.dumps(response))

    def toHashedBase64String(self, data: str):
        bytes_data = data.encode()
        hashed_data = sha256(bytes_data).digest()
        base64_data = b64encode(hashed_data)
        return base64_data.decode()

    def Reidentify(self):
        message = {"eventSubscriptions": self.getSubscriptionBitmask()}

        self.websocket_op.sendText(json.dumps(message))

    def getSubscriptionBitmask(self):
        bitmask = EventSubscription.ALL

        if self.parent_op.par.Includeinputvolumemeters:
            bitmask |= EventSubscription.INPUT_VOLUME_METERS
        if self.parent_op.par.Includeinputactivestatechanged:
            bitmask |= EventSubscription.INPUT_ACTIVE_STATE_CHANGED
        if self.parent_op.par.Includeinputshowstatechanged:
            bitmask |= EventSubscription.INPUT_SHOW_STATE_CHANGED
        if self.parent_op.par.Includesceneitemtransformchanged:
            bitmask |= EventSubscription.SCENE_ITEM_TRANSFORM_CHANGED

        return bitmask

    def SendRequest(self, typ, rid=str(uuid4()), data=None):
        self.parent_op.clearScriptErrors()

        if isinstance(typ, RequestType):
            typ = typ.value

        request = {
            "op": WebSocketOpCode.REQUEST,
            "d": {"requestType": typ, "requestId": rid, "requestData": data},
        }

        self.websocket_op.sendText(json.dumps(request))

    def SendRequestBatch(
        self,
        data,
        execution_type=RequestBatchExecutionType.SERIAL_REALTIME,
        halt_on_failure=False,
    ):
        self.parent_op.clearScriptErrors()

        if isinstance(data, abc.Sequence):
            for request in data:
                if isinstance(request["requestType"], RequestType):
                    request["requestType"] = request["requestType"].value

        request = {
            "op": WebSocketOpCode.REQUEST_BATCH,
            "d": {
                "requestId": str(uuid4()),
                "haltOnFailure": halt_on_failure,
                "executionType": execution_type,
                "requests": data,
            },
        }

        self.websocket_op.sendText(json.dumps(request))

    def HandleEvent(self, data: EventMessage):
        param_name = eventTypeToName(data["eventType"])

        if "eventData" in data:
            self.parent_op.par[param_name].val = data["eventData"]
        else:
            self.parent_op.par[param_name].pulse()
