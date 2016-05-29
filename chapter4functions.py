# -*- coding: utf-8 -*-
"""
Created on Sun May 29 10:27:24 2016

@author: Rahul Patni
"""

def ComputePay(hours, rate):
    overTime = hours - 40
    regularTime = 40
    return regularTime * rate + overTime * rate * 1.5
    
def ComputePayInput():
    try:
        hours = float(raw_input("Enter hours: "))
        rate = float(raw_input("Enter rate: "))
        print "Pay: ", ComputePay(hours, rate)
    except:
        print("Enter a valid number")    

def Grades(score):
        if (score > 1.0 or score < 0):
            print "Bad Score"
            GradesInput()
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
        
def GradesInput():
    try:
        score = float(raw_input("Enter your score:\n"))
        Grades(score)
    except: 
        print "Bad Score"
        GradesInput()

GradesInput()