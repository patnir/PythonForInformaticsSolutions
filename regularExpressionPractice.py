# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 20:31:43 2016

@author: Rahul Patni
"""

import re

hand = open('mbox-short.txt')


# searching if a line contains an expression
#for line in hand:
#    line = line.rstrip()
#    if re.search('From: ', line):
#        print line
        
        
# searching is a line starts with an expression
for line in hand:
    line = line.rstrip()
    if re.search('^From: ', line):
        print line
        
hand.seek(0) # go back to the beginning of the file

# wild card characters - starts with ^ and many times *
for line in hand:
    line = line.rstrip()
    if re.search('^X.*:', line):
        print line

hand.seek(0)

# Match the start of the line 'X-', Match any nonwhitespace character '\S'
# One or more times '+'
for line in hand:
    line = line.rstrip()
    if re.search('X-\S+', line):
        print line

hand.seek(0)

sptr = "My 2 favorite numbers are 25 and 56"
y = re.findall('[aeiou]+', sptr)
print y


# Greedy matching
for line in hand:
    line = line.rstrip()
    x = re.findall('^F.+:', line)
    if (x != []):
        print x

hand.seek(0)


# Non greedy matching

for line in hand:
    line = line.rstrip()
    x = re.findall('^F.+?:', line)
    if (x != []):
        print x

hand.seek(0)

# Removing email values

for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if (x != []):
        print x
hand.seek(0)

for line in hand:
    line = line.rstrip()
    x = re.findall('^From (\S+@\S+)', line)
    if (x != []):
        print x
hand.seek(0)

#finding domain name

for line in hand:
    line = line.rstrip()
    x = re.findall('^From .*@([^ ]*)', line)
    if (x != []):
        print x
hand.seek(0)