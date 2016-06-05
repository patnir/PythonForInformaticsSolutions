# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 16:14:56 2016

@author: Rahul Patni
"""

# Accessing APIs in Python

# REST - Representational State Transfer 
#   remote resources that we create, read, update and delete remotely

# Geocoding API Google

#import urllib
#import json
#
#serviceurl = "http://maps.googleapis.com/map/api/geocode/json?"
#
#while True:
#    address = raw_input("Enter location: ")
#    if len(address) == 0:
#        break
#    url = serviceurl + urllib.urlencode({'sensor' : 'false', 'address' : address})
#    print 'Retrieving', url
#    uh = urllib.urlopen(url)
#    data = uh.read()
#    
#    print 'Retrieved', len(data), 'characters'
#    try: js = json.loads(str(data))
#    except: js = None
#    if 'status' not in js or js['status'] != 'OK':
#        print '==== Failure To Retrieve ===='
#        print data
#        continue
#    print json.dumps(js, indent=4)
#
#    lat = js["results"][0]["geometry"]["location"]["lat"]
#    lng = js["results"][0]["geometry"]["location"]["lng"]
#    print 'lat',lat,'lng',lng
#    location = js['results'][0]['formatted_address']
#    print location
    
    
    
import urllib
import json

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    print json.dumps(js, indent=4)

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng
    location = js['results'][0]['formatted_address']
    print location
