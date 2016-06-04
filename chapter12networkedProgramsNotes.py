# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 20:22:07 2016

@author: Rahul Patni
"""

# socket is a connection
# socket - 2 computers talking through a network
# "an absratction that works like a phone call"

# TCP Port Number - application-specific or process-specific software 
# communications endpoint

# client initiates a connection
# a server reacts to it

# IP address is like the phone numbe of a computer
# equal to the domain name address

import socket #python library

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_socket.connect(('www.py4inf.com', 80))

# URL has three part - protocol, host, document
# URL - Uniform Resource Locator

# Request response cycle

my_socket.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    data = my_socket.recv(512)
    if (len(data) < 1):
        break;
    print data

my_socket.close()