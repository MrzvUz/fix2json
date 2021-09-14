#!/usr/bin/python3
# from fix_lib import quickfix
import quickfix as fix
import json
import xml.etree.ElementTree as ET
from collections import OrderedDict



def lambda_handler(event, context=None):
    try:
        # 1. Iterate over each record.
        for record in event["Records"]:
            # 2. Handle event type.
            if record["eventName"] == "INSERT":
                handle_insert(record)
    except Exception as e:
        print(e)
        return "Something went wrong."


def handle_insert(record):
    print("Handling INSERT event.")
    # 3a. Parse newImage content.
    newImage = record["dynamodb"]["NewImage"]
    # 3b. Parse the values.
    MsgData = newImage["MsgData"]["S"]
    # 3c. Print it out.
    print("New FIX message added with MsgData = " + MsgData)
    print("Done hangling INSERT event")


# string = handle_insert(record=True)

string = "8=FIX.4.4\0019=247\00135=s\00134=5\00149=sender\00152=20060319-09:08:20.881\00156=target\00122=8\00140=2\00144=9\00148=ABC\00155=ABC\00160=20060319-09:08:19\001548=184214\001549=2\001550=0\001552=2\00154=1\001453=2\001448=8\001447=D\001452=4\001448=AAA35777\001447=D\001452=3\00138=9\00154=2\001453=2\001448=8\001447=D\001452=4\001448=aaa\001447=D\001452=3\00138=9\00110=056\001"


# Load data dictionary.
data_dictionary_xml = "fix_lib/spec/FIX44.xml"

data_dictionary = fix.DataDictionary(data_dictionary_xml)
fix.Message().InitializeXML(data_dictionary_xml)

# String as fix message according to dictionary.
message = fix.Message(string, data_dictionary, True)

# Marked-up XML.
xml = message.toXML()
# Enable print(xml) to print xml format output.
# print(xml)


def get_field_type_map(data_dictionary_xml):
    """Preprocess DataDictionary to get field types."""
    field_type_map = {}
    with open(data_dictionary_xml, "r") as f:
        xml = f.read()
        tree = ET.fromstring(xml)
        fields = tree.find("fields")
        for field in fields.iter("field"):
            field_type_map[field.attrib["number"]] = field.attrib["type"]
    return field_type_map

field_type_map = get_field_type_map(data_dictionary_xml)

INT_TYPES = ["INT", "LENGTH", "NUMINGROUP", "QTY", "SEQNUM"]
FLOAT_TYPES = ["FLOAT", "PERCENTAGE", "PRICE", "PRICEOFFSET"]
BOOL_TYPES = ["BOOLEAN"]
DATETIME_TYPES = ["LOCALMKTDATE", "MONTHYEAR", "UTCDATEONLY", "UTCTIMEONLY", "UTCTIMESTAMP"]
STRING_TYPES = ["AMT", "CHAR", "COUNTRY", "CURRENCY", "DATA", "EXCHANGE", "MULTIPLEVALUESTRING", "STRING"]


def field_map_to_list(field_map, field_type_map):
    fields = []
    field_iter = iter([el for el in field_map if el.tag == "field"])
    group_iter = iter([el for el in field_map if el.tag == "group"])
    for field in field_iter:
        # Extract raw value.
        raw = field.text
        # Type the raw value.
        field_type = field_type_map.get(field.attrib["number"])
        if field_type in INT_TYPES:
            value = int(raw)
        elif field_type in FLOAT_TYPES:
            value = float(raw)
        elif field_type in BOOL_TYPES:
            value = bool(int(raw))
        elif field_type in DATETIME_TYPES:
            value = str(raw)
        elif field_type in STRING_TYPES:
            value = str(raw)
        else:
            value = str(raw)
        # field.attrib should contain "name", "number", "enum".
        _field = {
            **field.attrib,
            "type": field_type,
            "raw": raw,
            "value": value,
        }
        # If NUMINGROUP type then iterate groups the number indicated.
        # This assumes groups are in the same order as their field keys.
        if field_type == "NUMINGROUP":
            groups = []
            for _ in range(value):
                group = next(group_iter)
                # Parse group as field map.
                group_fields = field_map_to_list(group, field_type_map)
                groups.append(group_fields)
            _field["groups"] = groups
        fields.append(_field)
    return fields


def field_map_to_dict(field_map, field_type_map):
    fields = OrderedDict()
    field_iter = iter([el for el in field_map if el.tag == "field"])
    group_iter = iter([el for el in field_map if el.tag == "group"])
    for field in field_iter:
        # Define key.
        # field.attrib should contain "name", "number", "enum".
        key = field.attrib.get("name") or field.attrib.get("number")
        # Extract raw value.
        raw = field.text
        # Type the raw value.
        field_type = field_type_map.get(field.attrib["number"])
        if field_type in INT_TYPES:
            value = int(raw)
        elif field_type in FLOAT_TYPES:
            value = float(raw)
        elif field_type in BOOL_TYPES:
            value = bool(int(raw))
        elif field_type in DATETIME_TYPES:
            value = str(raw)
        elif field_type in STRING_TYPES:
            value = str(raw)
        else:
            value = str(raw)
        # If NUMINGROUP type then iterate groups the number indicated.
        # This assumes groups are in the same order as their field keys.
        if field_type == "NUMINGROUP":
            groups = []
            for _ in range(value):
                group = next(group_iter)
                # Parse group as field map.
                group_fields = field_map_to_dict(group, field_type_map)
                groups.append(group_fields)
            fields[key] = groups
        else:
            # Preference enum above value.
            fields[key] = field.attrib.get("enum") or value
    return fields


def parse_message_xml(xml, field_type_map, as_dict=False):
    parsed = OrderedDict()
    tree = ET.fromstring(xml)
    for field_map in tree:
        if not as_dict:
            parsed[field_map.tag] = field_map_to_list(field_map, field_type_map)
        else:
            parsed[field_map.tag] = field_map_to_dict(field_map, field_type_map)
    return parsed

# # List of fields (groups embedded).
# parsed = parse_message_xml(xml, field_type_map, as_dict=False)
# print(json.dumps(parsed, indent=True))

print("-------------------------------------------")

# JSON-like output.
parsed = parse_message_xml(xml, field_type_map, as_dict=True)
print(json.dumps(parsed, indent=True))

print("-------------------------------------------")

