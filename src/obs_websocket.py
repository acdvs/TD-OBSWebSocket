from base64 import b64encode
from hashlib import sha256
import json
from typing import Any
from uuid import uuid4
from packaging.version import Version

from component_builder import build_event_pars, event_type_to_name
from obs_enums import (
    RequestStatus,
    WebSocketOpCode,
    EventSubscription,
    RequestType,
    RequestBatchExecutionType,
)
from obs_request import Request
from obs_schema import EventMessage, HelloMessage


class OBSWebSocket:
    def __init__(self, parent_op: baseCOMP):
        self.parent_op = parent_op
        self.websocket_op = op("websocket").asType(websocketDAT)
        self.responses_op = op("responses").asType(tableDAT)

        self.parent_op.par.Connected = False

        self.websocket_op.clear()
        self.responses_op.clear(keepFirstRow=True)

        self.Request = Request
        self.RequestBatchExecutionType = RequestBatchExecutionType
        self.RequestStatus = RequestStatus
        self.RequestType = RequestType

    def Identify(self, data: HelloMessage):
        obs_websocket_version = Version(data["obsWebSocketVersion"])
        build_event_pars(obs_websocket_version)

        response = {
            "op": WebSocketOpCode.IDENTIFY,
            "d": {
                "rpcVersion": 1,
                "eventSubscriptions": self.__get_subscription_bitmask(),
            },
        }

        if "authentication" in data:
            secret = base64_hash(
                self.parent_op.par.Password + data["authentication"]["salt"]
            )
            auth = base64_hash(secret + data["authentication"]["challenge"])

            response["d"]["authentication"] = auth

        self.websocket_op.sendText(json.dumps(response))

    def Reidentify(self):
        message = {"eventSubscriptions": self.__get_subscription_bitmask()}

        self.websocket_op.sendText(json.dumps(message))

    def __get_subscription_bitmask(self):
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

    def HandleEvent(self, data: EventMessage):
        param_name = event_type_to_name(data["eventType"])

        if "eventData" in data:
            self.parent_op.par[param_name].val = data["eventData"]
        else:
            self.parent_op.par[param_name].pulse()

    def __send_request(self, data: dict[str, Any]):
        sent_bytes = self.websocket_op.sendText(json.dumps(data))
        return True if sent_bytes >= 0 else False

    def SendRequest(self, request: Request):
        """
        Send a request to OBS.
        ### Returns
        A boolean indicating success.
        """
        data = request.build()
        return self.__send_request(data)

    def SendBatchRequest(
        self,
        requests: list[Request],
        execution_type: RequestBatchExecutionType = RequestBatchExecutionType.SERIAL_REALTIME,
        halt_on_failure: bool = False,
        id: str = None,
    ):
        """
        Send multiple requests to OBS.
        ### Arguments
        - `requests` - The `Request`s to send.
        - `execution_type` - The [batch execution type](https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#requestbatchexecutiontype). Defaults to standard serial execution.
        - `halt_on_failure` - If true, stop processing if one request fails.
        - `id` - A batch request ID . Directly returned in the response. Useful for distinguishing batch requests. This ID is separate from request IDs within the batch.
        ### Returns
        A boolean indicating success.
        """
        if len(requests) == 0:
            raise ValueError("No requests passed to SendBatchRequest.")

        request_data = [request.build_data() for request in requests]

        batch_data = {
            "op": WebSocketOpCode.REQUEST_BATCH,
            "d": {
                "executionType": execution_type.value,
                "haltOnFailure": halt_on_failure,
                "requestId": id or str(uuid4()),
                "requests": request_data,
            },
        }

        print(json.dumps(batch_data))

        return self.__send_request(batch_data)


def base64_hash(data: str):
    bytes_data = data.encode()
    hashed_data = sha256(bytes_data).digest()
    base64_data = b64encode(hashed_data)
    return base64_data.decode()
