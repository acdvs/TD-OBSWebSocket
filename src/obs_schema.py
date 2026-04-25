import json
from typing import Any, NotRequired, TypedDict
import urllib.request

from obs_enums import RequestType, RequestStatus as RequestStatusCode


# Messages


class BaseMessage(TypedDict):
    op: int
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


class RequestMessage(TypedDict):
    requestType: RequestType
    requestId: str
    requestData: dict[str, Any]


class RequestStatus(TypedDict):
    result: bool
    code: RequestStatusCode
    comment: NotRequired[str]


class RequestResponseMessage(TypedDict):
    requestType: RequestType
    requestId: str
    requestStatus: RequestStatus
    responseData: dict[str, Any]


class RequestBatchResponseMessage(TypedDict):
    requestId: str
    results: list[RequestResponseMessage]


# Structures


class EnumIdentifier(TypedDict):
    description: str
    enumIdentifier: str
    rpcVersion: int
    deprecated: bool
    initialVersion: str
    enumValue: int | str


class OBSEnum(TypedDict):
    enumType: str
    enumIdentifiers: list[EnumIdentifier]


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


class Schema(TypedDict):
    events: list[Event]


# Utils


def load_schema() -> Schema:
    schema_url = parent().fetch("schema_url")

    with urllib.request.urlopen(schema_url) as res:
        return json.load(res)
