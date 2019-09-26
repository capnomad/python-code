import urllib.request, urllib.parse, urllib.error
import json
import ssl


url = "http://py4e-data.dr-chuck.net/comments_42.json"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


data = urllib.request.urlopen(url, context=ctx).read()
print(data)