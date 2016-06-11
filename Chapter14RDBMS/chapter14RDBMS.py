# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 19:58:29 2016

@author: Rahul Patni
"""

# Chapter 14 Relational Databases 

# Terminology - Database (or collection of tables), Relation (or table), 
# Tuple (or row), Attribute (or column)

# SQL - Structured Query Language - issue commands to a database
# Database application - use of abstraction to communicate with the database
# APIs exist to help communication

'''
CREATE TABLE Users (
name VARCHAR(128), email VARCHAR(128)
)
'''

import sqlite3
import re

conn = sqlite3.connect('domainCountAnswer.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = raw_input('Enter file name: ')
if (len(fname) < 1) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    line = line.rstrip()
    if not line.startswith('From: '):
        continue
    x = re.findall('[@]([a-z.]+)', line)
    if (x == []):
        continue
    org = x[0]
    print org
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES ( ?, 1)', (org, ))
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
                    (org, ))
conn.commit()
    
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
print 
print "Counts:"
for row in cur.execute(sqlstr):
    print str(row[0]), row[1]

cur.close()
    
    
    
    
    
    
    
    
    
        