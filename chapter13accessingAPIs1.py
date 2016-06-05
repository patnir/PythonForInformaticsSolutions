# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 17:22:30 2016

@author: Rahul Patni
"""

import urllib
import json

url = raw_input('Enter location:')
if len(url) == 0: 
    url = "http://python-data.dr-chuck.net/comments_280615.json"
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
js = json.loads(str(data))
total = 0
for i in js['comments']:
    total += int(i['count'])
print total