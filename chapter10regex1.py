# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 22:42:11 2016

@author: Rahul Patni
"""
import re

def countNumbersInFile():
    fhandle = open('regex_sum_280609.txt')
    total = 0
    for line in fhandle:
        line = line.rstrip()
        x = re.findall('[0-9]+', line)
        if (x != []):
            for i in x:
                total += int(i)
    print total
    
countNumbersInFile()