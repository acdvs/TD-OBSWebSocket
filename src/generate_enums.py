import re
from typing import Any

from obs_schema import load_schema

schema = load_schema()

lines: list[str] = []
enum_imports = ["unique"]

r_word_boundary = re.compile(r"([a-z])([A-Z])")
r_non_word = re.compile(r"\W+")


def to_valid_identifier(s: str) -> str:
    s1 = re.sub(r_word_boundary, r"\1_\2", s)
    s2 = re.sub(r_non_word, "_", s1)
    return s2.upper()


def get_superclass_name(val: Any):
    if type(val) is int:
        return "IntEnum"
    else:
        return "Enum"


def append_class(name: str, superclass: str, lst: list, keyKey: str, valKey: str):
    lines.append("")
    lines.append("@unique")
    lines.append(f"class {name}({superclass}):")

    for entry in lst:
        key = to_valid_identifier(entry[keyKey])
        val = format_value(entry[valKey])
        description = re.sub(r"\n(    )?", "\n    ", entry["description"])

        lines.append(f"    {key} = {val}")
        lines.append(f"    '''")
        lines.append(f"    {description}")
        lines.append(f"    ")
        lines.append(f"    Initial version: {entry['initialVersion']}")
        lines.append(f"    '''")


def format_value(val):
    if type(val) is str:
        if val.startswith("("):
            val = val[1:-1]

        if val.find("|") >= 0:
            parts = val.split("|")
            parts = [to_valid_identifier(p.strip()).upper() for p in parts]
            return " | ".join(parts)

        try:
            eval(val)
            return val
        except:
            return repr(val)
    else:
        return str(val)


for enum in schema["enums"]:
    name = enum["enumType"]
    idents = enum["enumIdentifiers"]
    superclass = get_superclass_name(idents[0]["enumValue"])

    if superclass not in enum_imports:
        enum_imports.append(superclass)

    append_class(name, superclass, idents, "enumIdentifier", "enumValue")

append_class("RequestType", "Enum", schema["requests"], "requestType", "requestType")

enum_imports_str = "from enum import " + ", ".join(enum_imports)
lines.insert(0, enum_imports_str)

code = "\n".join(lines)

with open("../src/obs_enums.py", "w") as f:
    f.write(code)
