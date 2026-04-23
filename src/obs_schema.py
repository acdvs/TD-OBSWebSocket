import json
import re
from typing import Any, NotRequired, TypedDict
import urllib.request


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


def loadSchema() -> Schema:
    schema_url = parent().fetch("schema_url")

    with urllib.request.urlopen(schema_url) as res:
        return json.load(res)


def generateEnums():
    print("test")

    lines: list[str] = []
    schema = loadSchema()
    enum_imports = ["unique", "Enum"]

    r_word_boundary = re.compile(r"([a-z])([A-Z])")
    r_non_word = re.compile(r"\W+")

    def to_valid_identifier(s: str) -> str:
        s1 = re.sub(r_word_boundary, r"\1_\2", s)
        s2 = re.sub(r_non_word, "_", s1)
        return s2.upper()

    def get_superclass_name(val: Any):
        if type(val) == int:
            return "IntEnum"
        else:
            return "Enum"

    def append_class(name: str, superclass: str):
        lines.append("")
        lines.append("@unique")
        lines.append(f"class {name}({superclass}):")

    for enum in schema["enums"]:
        name = enum["enumType"]
        idents = enum["enumIdentifiers"]
        superclass = get_superclass_name(idents[0]["enumValue"])
        entries: dict[str, Any] = {}

        if superclass not in enum_imports:
            enum_imports.append(superclass)

        append_class(name, superclass)

        for ident in idents:
            key = to_valid_identifier(ident["enumIdentifier"])
            val = ident["enumValue"]

            try:
                val = eval(val)
            except:
                if superclass == "IntEnum" and type(val) == str:
                    val = val[1:-1]
                    total = 0

                    for k in val.split("|"):
                        total |= entries[to_valid_identifier(k.strip())]

                    val = total

            lines.append(f"    {key} = {repr(val)}")
            entries[key] = val

    append_class("RequestType", "Enum")

    for req in schema["requests"]:
        key = to_valid_identifier(req["requestType"])
        val = req["requestType"]
        lines.append(f"    {key} = '{val}'")

    enum_imports_str = "from enum import " + ", ".join(enum_imports)
    lines.insert(0, enum_imports_str)

    code = "\n".join(lines)

    op("obs_enums").asType(textDAT).text = code
