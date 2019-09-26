import json

data = '''
{
    "name": "John",
    "phone": {
        "type": "intl",
        "number": "+91 1234567890"
    },
    "email": {
        "hide": "yes"
    }
}
'''



info = json.loads(data)
print(type(data))
print(type(info))
print(info)
print("name:", info["name"])
print("phone:", info["phone"]["number"])

