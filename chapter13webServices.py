# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 14:14:45 2016

@author: Rahul Patni
"""

import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location:')
if len(url) == 0: 
    url = "http://python-data.dr-chuck.net/comments_280611.xml"
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
counts = tree.findall('.//count')
total = 0
for i in counts:
    total += int(i.text)

print total