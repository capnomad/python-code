#parsing xml in python

import xml.etree.ElementTree as ET

data = '''
<contact>
    <persons>
        <person>
            <name>John</name>
            <phone type="intl">9876543210</phone>
            <email hide="yes"/>
        </person>
        <person>
            <name>Wick</name>
            <phone type="intl">1234567890</phone>
            <email hide="no"/>
        </person>
    </persons>
</contact>
'''

tree = ET.fromstring(data)
lst = tree.findall('persons/person')
print("count: ", len(lst))

for item in lst:
    print("Name: ",item.find("name").text)
    print("Phone: ",item.find("phone").text)
    print("Email hidden: ",item.find("email").get("hide"))