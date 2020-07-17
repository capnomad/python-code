import urllib.parse, urllib.request, urllib.error

from bs4 import BeautifulSoup
import ssl

#ignore ssl certificates that are not in python's official list which may cause trouble
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "http://www.dr-chuck.com/page1.htm"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


tags = soup('a')
print(tags)
for tag in tags:
    print(tag.get('href',None))

