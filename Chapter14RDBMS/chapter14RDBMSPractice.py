# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:48:26 2016

@author: Rahul Patni
"""
import re

count = 0

fname = raw_input('Enter file name: ')
if (len(fname) < 1) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    line = line.rstrip()
    x = re.findall('[@]([a-z.]+)', line)
    if (x != []):
        print x[0]
        count += 1
    if (count == 50):
        break
        