# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 22:02:22 2016

@author: Rahul Patni
"""

import urllib
from bs4 import *

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "lxml")

tags = soup('a')

for tag in tags:
    print tag.get('href', None)