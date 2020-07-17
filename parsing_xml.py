#parsing xml in python

import xml.etree.ElementTree as ET

data = '''
<person>
    <name>John</name>
    <phone type="intl">9876543210</phone>
    <email hide="yes"/>
</person>
'''

tree = ET.fromstring(data)
print("Name: ",tree.find("name").text)
print("Phone: ",tree.find("phone").text)
print("Email hidden: ",tree.find("email").get("hide"))