# -*- coding: utf-8 -*-
"""
Created on Mon May 30 14:27:12 2016

@author: Rahul Patni
"""

'''
Tuples are immutable, like strings
Cannot sort, append to tuples
Can find the count and index
They are quicker, use less memory, not dynamic that like lists
From a dictionary d, we can get a list of tuples (which contains a value and an 
index)
They are comparable, they compare the left most thing, if they are equal they
move right - return True or False based on the comparison

We CAN sort a list of tuples!!! We can sort by key

tmp.sort(reverse == True) # To sort by reverse

'''

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dayCount = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        check = line.split()
        time = check[5].split(':')
        hour = time[0]
        dayCount[hour] = dayCount.get(hour, 0) + 1
tup = dayCount.items()
tup.sort()
for k, v in tup:
    print k, v
        