import urllib
import re
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('td')
total = 0
for tag in tags:
    # Look at the parts of a tag
    line = 'Contents:',tag.contents[0]
    #print str(line[1])
    x = re.findall('[0-9]+', str(line))
    if (x != []):
        total += int(x[0])
print total
        
