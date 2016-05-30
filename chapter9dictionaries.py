# -*- coding: utf-8 -*-
"""
Created on Mon May 30 13:52:46 2016

@author: Rahul Patni
"""

# Exercise 9.3
def findDaysOfWeek():
    fname = 'mbox-short.txt'
    f = open(fname)
    daysOfWeek = dict()
    for line in f:
        line = line.strip()
        if line.startswith("From "):
            check = line.split()
            daysOfWeek[check[2]] = daysOfWeek.get(check[2],0) + 1  
    print daysOfWeek
            
# findDaysOfWeek()
  
# Exercise 9.4          
def findMaxEmailsSent():
    fname = 'mbox-short.txt'
    f = open(fname)
    daysOfWeek = dict()
    for line in f:
        line = line.strip()
        if line.startswith("From "):
            check = line.split()
            daysOfWeek[check[1]] = daysOfWeek.get(check[1],0) + 1  
    ids = daysOfWeek.keys()
    number = daysOfWeek.values()
    for i in number:
        if number[i] == max(number):
            print ids[i], number[i]
            break
        
    
    
# findMaxEmailsSent()
    
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
f = open(name)
daysOfWeek = dict()
for line in f:
    line = line.strip()
    if line.startswith("From "):
        check = line.split()
        daysOfWeek[check[1]] = daysOfWeek.get(check[1],0) + 1  
ids = daysOfWeek.keys()
number = daysOfWeek.values()
maximum = max(number)
for i in range(len(number)):
    if number[i] == maximum:
        print ids[i], number[i], "dasd"
        break
    
