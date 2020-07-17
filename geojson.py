import urllib.parse, urllib.request, urllib.error
import json

#my key:AIzaSyAC6B9Ymv3MzRycIxPEOdgfdSFKBaDr8Ss


serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

address = "Katni"

url = serviceurl + urllib.parse.urlencode(
    {"address": address}
)
print(url)


