#!/Users/cemakay/Python/.venv/bin/python

import json
print(json)
print(type(json))

json_string = '{"Name": "John", "Age": 30, "City": "New Tork"}'

data = json.loads(json_string)

print(data)
print(type(data))
