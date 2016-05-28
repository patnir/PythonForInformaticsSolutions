# -*- coding: utf-8 -*-
"""
Created on Sat May 28 14:34:22 2016

@author: Rahul Patni
"""

def nameIO():
    name = raw_input("Enter your name: ")
    print name    


def rateIO():
    hours = float(raw_input("Enter hours: "))
    rate = float(raw_input("Enter rate: "))
    print "Pay: ", hours * rate
    
def celciusConvert():
    temperature = float(raw_input("Enter a temperature in Celcius: "))
    print "Temperature in Fahrenheit: ", temperature * 9 / 5 + 32

celciusConvert()