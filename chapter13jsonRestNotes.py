# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 14:55:11 2016

@author: Rahul Patni
"""

# JSON and REST architecture

# JSON solves the same problem, but JSON does not do as well in terms of infinitely nested things
# IT is a not as good at "self-describing"

# JSON has 2 basic structures - a list (array) or dictionary (object)

import json

data = '''{
    "name" : "Rahul",
    "phone" : {
        "type" : "intl",
        "number" : "+1 123 123 1234"
        },
    "email" : {
        "hide" : "yes"        
    }    
}'''

info = json.loads(data)
print info
print 'Name:', info["name"]
print 'Hide:', info["email"]["hide"]

input = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  } 
]'''

info = json.loads(input)
print info
print 'User count:', len(info)

for item in info:
    print 'Name', item['name']
    print 'Id', item['id']
    print 'Attribute', item['x']


# Service oriented approach
# Taking data from many sources and putting them together

# Most non trivial web applications use services from other applications like
# Credit card charge, hotel reservation systems

# Services publish the "rules" applications must follow to make use of the services (API)