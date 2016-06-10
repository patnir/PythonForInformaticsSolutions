# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 19:08:44 2016

@author: Rahul Patni
"""

# Chapter 13.5
# Object Oriented Programming 

# Objects are self-contained code and data, Objects have boundaries that allow 
# us to ignore uneeded detail
# Helps break problems into smaller chunks to make it more understandable

# Terminology = Class, Method, Field or attribute, Object or the Instance

# A useless example

class Fan:
    x = 0
    name = ""
    def __init__(self, name):
        print "Constructed"
        self.name = name
        
    def party(self):
        self.x += 1
        print "Count", self.x, self.name

    # destructor code
    # def __del__(self):
    #    print "Destructed", self.x


# instances of the same class are independent

an = Fan("joker")

an.party()
an.party()
an.party()
an.party()

# another way to achieve the above result

Fan.party(an)

# Object lifecycle

# Constructor, set up the parameters to have initial values


class FootballFan(Fan):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print self.name, self.points, self.x

an2 = FootballFan("classy")
an2.touchdown()





print dir(Fan)

