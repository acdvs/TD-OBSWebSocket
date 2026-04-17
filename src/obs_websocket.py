from base64 import b64encode
from collections import abc
from hashlib import sha256
import json
from uuid import uuid4

from component_builder import buildEventPars, eventTypeToName
from obs_enums import (
	WebSocketOpCode,
	EventSubscription,
	RequestType,
	RequestBatchExecutionType,
)

class OBSWebSocket(baseCOMP):
	def __init__(self, parentComp: baseCOMP):
		self.parentComp = parentComp
		self.websocket = op("websocket").asType(websocketDAT)

		self.RequestType = RequestType
		self.RequestBatchExecutionType = RequestBatchExecutionType

		self.parentComp.par.Connected = False
		self.websocket.clear()

		responses = op("request_responses").asType(tableDAT)
		responses.clear(keepFirstRow=True)

	def Identify(self, data):
		buildEventPars(data["obsWebSocketVersion"])

		response = {
			"op": WebSocketOpCode.IDENTIFY,
			"d": {"rpcVersion": 1, "eventSubscriptions": self.getSubscriptionBitmask()},
		}

		if "authentication" in data:
			secret = b64encode(
				sha256(
					(
						self.parentComp.par.Password + data["authentication"]["salt"]
					).encode()
				).digest()
			)

			auth = b64encode(
				sha256(
					(secret.decode() + data["authentication"]["challenge"]).encode()
				).digest()
			).decode()

			response["d"]["authentication"] = auth

		self.websocket.sendText(json.dumps(response))

	def Reidentify(self):
		message = {"eventSubscriptions": self.getSubscriptionBitmask()}

		self.websocket.sendText(json.dumps(message))

	def getSubscriptionBitmask(self):
		bitmask = EventSubscription.ALL

		if self.parentComp.par.Includeinputvolumemeters:
			bitmask |= EventSubscription.INPUT_VOLUME_METERS
		if self.parentComp.par.Includeinputactivestatechanged:
			bitmask |= EventSubscription.INPUT_ACTIVE_STATE_CHANGED
		if self.parentComp.par.Includeinputshowstatechanged:
			bitmask |= EventSubscription.INPUT_SHOW_STATE_CHANGED
		if self.parentComp.par.Includesceneitemtransformchanged:
			bitmask |= EventSubscription.SCENE_ITEM_TRANSFORM_CHANGED

		return bitmask

	def SendRequest(self, typ, rid=str(uuid4()), data=None):
		self.parentComp.clearScriptErrors()

		if isinstance(typ, RequestType):
			typ = typ.value

		request = {
			"op": WebSocketOpCode.REQUEST,
			"d": {"requestType": typ, "requestId": rid, "requestData": data},
		}

		self.websocket.sendText(json.dumps(request))

	def SendRequestBatch(
		self,
		data,
		executionType=RequestBatchExecutionType.SERIAL_REALTIME,
		haltOnFailure=False,
	):
		self.parentComp.clearScriptErrors()

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

		self.websocket.sendText(json.dumps(request))

	def HandleEvent(self, data):
		paramName = eventTypeToName(data["eventType"])
		eventData = data["eventData"] if "eventData" in data else True

		if "eventData" in data:
			self.parentComp.par[paramName].val = eventData
		else:
			self.parentComp.par[paramName].pulse()
