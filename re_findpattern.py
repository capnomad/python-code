import re

s = "<p>Please click <a href=\"http://www.dr-chuck.com\">here</a></p>"

print(re.findall('href="(.+)"',s))
print(re.findall('href=".+"',s))
print(re.findall('http://.*',s))
print(re.findall('<.*>',s))

