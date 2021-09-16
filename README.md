Depending on the user's need there are three solutions presented here.

    1. Marked-up XML
    2. List of fields (groups embedded).
    3. JSON-like output.

In the quickfix Python library, the FieldMap field and group key iterators are not exposed. So the approach is to first generate the XML and iterate over the tree. There is also no access to the getFieldType method of the DataDictionary, so the dictionary must be pre-processed to store the field types for conversion and handling of groups.

RUN from fix2json-py-v2 folder:
╰─ $./fix2json.py --spec spec/FIX44.xml
