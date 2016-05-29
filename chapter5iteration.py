# -*- coding: utf-8 -*-
"""
Created on Sun May 29 10:48:20 2016

@author: Rahul Patni
"""
import sys

def numberUntilDone():
    total = 0
    count = 0
    minimum = sys.maxint
    maximum = -sys.maxint - 1
    while True:    
        try:
            number = raw_input("Enter a number: ")
            if (number == "done"):
                break
            number = int(number)
            if (number > maximum):
                maximum = number
            if (number < minimum):
                minimum = number
            total = total + number
            count = count + 1
        except:
            print "Invalid Input"
    print "Total = ", total
    print "Count = ", count
    print "Average = ", round(float(total) / count, 3)
    print "Maximum = ", maximum
    print "Minimum = ", minimum
    
numberUntilDone()
    
