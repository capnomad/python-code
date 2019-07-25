import urllib.parse, urllib.request, urllib.error

from bs4 import BeautifulSoup
import ssl
import re

#ignore ssl certificates that are not in python's official list which may cause trouble
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#url = "http://py4e-data.dr-chuck.net/comments_42.html"
#url = "http://py4e-data.dr-chuck.net/comments_227442.html"
url = input("Enter - ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0
count = 0
tags = soup('span')
for tag in tags:
    sum += int(tag.contents[0])
    count += 1
print("Count", count)
print("Sum", sum)




