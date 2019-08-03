import urllib.request
import urllib.parse
import urllib.error
import xml.etree.cElementTree as ET
import ssl

#url = "http://py4e-data.dr-chuck.net/comments_42.xml"
url = input("Enter location: ")

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0
count = 0

fh = urllib.request.urlopen(url)
data = ""
for line in fh:
    data += line.decode()

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')

for item in lst:

    sum = sum + int(item.find('count').text)
    count = count+1

print("Count: ", len(lst))
print("Sum: ", sum)
