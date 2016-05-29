# -*- coding: utf-8 -*-
"""
Created on Sun May 29 11:33:04 2016

@author: Rahul Patni
"""

def FindPartsOfEmail():
    email = raw_input("Enter your email address: ")
    email = email.strip()
    atPosition = email.find('@')
    dotPosition = email.find('.', atPosition)
    if (atPosition <= 0 or dotPosition - atPosition <= 1):
        print "Invalid email"
        return
    username = email[0:atPosition]
    domain = email[atPosition + 1 : dotPosition]
    extension = email[dotPosition + 1 : len(email)]
    print "Username:".ljust(10), username
    print "Domain:".ljust(10), domain
    print "Extension:".ljust(10), extension
    
FindPartsOfEmail()

def courseraAssignment():
    text = "X-DSPAM-Confidence:    0.8475";
    number = text[text.find(':') + 1 : len(text)].strip()
    print float(number)
    
