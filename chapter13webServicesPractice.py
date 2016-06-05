# -*- coding: utf-8 -*-
"""
Created on Sat Jun 04 19:25:55 2016

@author: Rahul Patni
"""
# Webservices - hand data from application
# Ways to structure the data - Wire format
# XML - Extensible Markup Program
# JSON - Javasciprt Object Notation (looks like a pyton dictionary)

# Wire Format - Serialize creating wire formart
# Deserialize - Converting wire format

# XML - tree structure of nodes
# Google - XML pretty printer

# Schema - proper shape
# ISO 8601 Date time format 2015-06-05T14:25:00Z

# Parsing XML in python

import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print 'Name:',tree.find('name').text
print 'Attr:',tree.find('email').get('hide')

import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
            </user>
        </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print 'User count:', len(lst)

for item in lst:
    print 'Name', item.find('name').text
    print 'Id', item.find('id').text
    print 'Attribute', item.get("x")

