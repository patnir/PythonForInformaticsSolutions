# -*- coding: utf-8 -*-
"""
Created on Sun May 29 12:44:19 2016

@author: Rahul Patni
"""
'''
7.1 Write a program that prompts for a file name, then opens that file and reads 
through the file, and print the contents of the file in upper case. Use the file 
words.txt to produce the output below.
'''

    
def fileContentsToUpper():
    # Use words.txt as the file name
    fname = raw_input("Enter file name: ")
    fh = open(fname)
    
    for line in fh:
        print line.rstrip().upper()
        
#fileContentsToUpper()

def averageSpamDifference():
    # Use the file name mbox-short.txt as the file name
    fname = raw_input("Enter file name: ")
    fh = open(fname)
    total = 0
    count = 0
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:") : continue
        check = line.rstrip()
        #print check
        colonPosition = check.find(':')
        number = float(check[colonPosition + 1: len(check)])
        total = total + number
        count = count + 1            
    print "Average spam confidence:", total / count
    
averageSpamDifference()

