import json
from typing import Any, NotRequired, TypedDict
import urllib.request

from obs_enums import WebSocketOpCode


def loadSchema():
    schema_url = parent().fetch("schema_url")

    with urllib.request.urlopen(schema_url) as res:
        return json.load(res)


# Messages


class BaseMessage(TypedDict):
    op: WebSocketOpCode
    d: dict[str, Any]


class Auth(TypedDict):
    challenge: str
    salt: str


class HelloMessage(TypedDict):
    obsStudioVersion: str
    obsWebSocketVersion: str
    rpcVersion: int
    authentication: NotRequired[Auth]


class EventMessage(TypedDict):
    eventType: str
    eventIntent: str
    eventData: dict[str, Any]


class RequestStatus(TypedDict):
    result: bool
    code: int
    comment: NotRequired[str]


class RequestResponseMessage(TypedDict):
    requestType: str
    requestId: str
    requestStatus: RequestStatus
    responseData: dict[str, Any]


class RequestBatchResponseMessage(TypedDict):
    requestId: str
    results: list[RequestResponseMessage]


# Structures


class DataField(TypedDict):
    valueName: str
    valueType: str
    valueDescription: str


class Event(TypedDict):
    description: str
    eventType: str
    eventSubscription: str
    complexity: int
    rpcVersion: str
    deprecated: bool
    initialVersion: str
    category: str
    dataFields: list[DataField]
