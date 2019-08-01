# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#start
#url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
#actual problem: http://py4e-data.dr-chuck.net/known_by_Rameesah.html 
#url = "http://py4e-data.dr-chuck.net/known_by_Rameesah.html" 
#url = input('Enter - ')

url = str(input("Enter URL: "))
count=int(input("Enter count: "))
position=int(input("Enter position: "))


i = 0
names = list()
while i < count:
  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')

  # Retrieve all of the anchor tags
  tags = soup('a')
  url = tags[position-1].get('href', None)
  print("Retrieving: ",url)
  names.append(tags[position -1].contents)
  i = i+1
ans = str(names[-1])
print(ans)