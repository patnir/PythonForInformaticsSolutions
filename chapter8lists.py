# -*- coding: utf-8 -*-
"""
Created on Mon May 30 11:13:16 2016

@author: Rahul Patni
"""

def readAndSortFileDate():
    fname = raw_input("Enter a filename: ")
    fh = open(fname)
    lst = list()
    for line in fh:
        for word in line.rstrip().split():
            if word not in lst:
                lst.append(word)
    lst.sort()     
    print lst
    
#readAndSortFileDate()

def obtainSenderEmailAddress():
    fname = 'mbox-short.txt' #raw_input("Enter file name: ")
    if len(fname) < 1 : fname = "mbox-short.txt"
    
    fh = open(fname)
    count = 0
    
    for line in fh:
        line = line.rstrip()
        if line.startswith('From:'):
            words = line.split()
            print words[1]
            count += 1
    print "There were", count, "lines in the file with From as the first word"

#obtainSenderEmailAddress()

