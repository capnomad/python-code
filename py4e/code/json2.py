import json

data = '''
[{
    "name": "John",
    "phone": {
        "type": "intl",
        "number": "+91 1234567890"
    },
    "email": {
        "hide": "yes"
    }
},
{
    "name": "Jim",
    "phone": {
        "type": "local",
        "number": "+91 9876543210"
    },
    "email": {
        "hide": "no"
    }
}]
'''



info = json.loads(data)
print(type(data))
print(type(info))
print("User count: ", len(info))
for item in info:
    print("Name: ", item['name'])
    print("Phone: ", item['phone']['number'])