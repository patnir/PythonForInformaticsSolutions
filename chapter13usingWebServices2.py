"""
Created on Fri Jun 03 23:06:08 2016

@author: Rahul Patni
"""

import urllib
from BeautifulSoup import *

def getTag(url, position):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)  
    # Retrieve all of the anchor tags 
    tags = soup('a')
    for tag in tags:
        position -= 1
        if (position == 0):
            return tag.get('href', None)
    
    
url = raw_input('Enter url - ')   
position = int(raw_input('Enter position - '))
count = int(raw_input('Enter count - ')) 

print "Retrieving:", url 
for i in range(count):
    url = getTag(url, position)
    print "Retrieving:", url