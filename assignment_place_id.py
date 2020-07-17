#url=http://py4e-data.dr-chuck.net/json?

import urllib.request, urllib.parse, urllib.error
import json
import ssl


api_key = 42
url = "http://py4e-data.dr-chuck.net/json?"


#ignore ssl error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#address = "South Federal University"
address = input("Enter location: ")
if len(address) < 1:
  print("no address")
  

param = dict()

param['address'] = address
param['key'] = api_key

url_1 = url + urllib.parse.urlencode(param)

print("Retrieving : ", url_1)
try:
  uh = urllib.request.urlopen(url_1, context=ctx)
  data = uh.read().decode()
except:
  print("Unable to open URL")


print("retrieved", len(data), "characters" )

js = json.loads(data)

#print(json.dumps(js, indent=4))
for i in js['results']:
  print(i['place_id'])
