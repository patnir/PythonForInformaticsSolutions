# -*- coding: utf-8 -*-
"""
Created on Sat May 28 14:35:54 2016

@author: Rahul Patni
"""

def celciusConvert():
    try:
        temperature = float(raw_input("Enter a temperature in Celcius: \n"))
        print "Temperature in Fahrenheit: \n", temperature * 9 / 5 + 32
    except:
        print "Enter a number for temperature."
        celciusConvert()
        
# celciusConvert()
        
        
def grades():
    try:
        score = float(raw_input("Enter your score:\n"))
        if (score > 1.0):
            raise Exception()
        elif (score >= 0.9):
            print "A"
        elif (score >= 0.8):
            print "B"
        elif (score >= 0.8):
            print "C"
        elif (score >= 0.8):
            print "D"
        else:
            print "F"
    except:
        print "Enter a score between 0.0 and 1.0"
        grades()

grades()