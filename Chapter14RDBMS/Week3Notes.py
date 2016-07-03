# -*- coding: utf-8 -*-
"""
Created on Sun Jul 03 07:31:19 2016

@author: Rahul Patni
"""

# Designing a Database Model and linking multiple tables (Relational SQL)

# Always start with a basic visual design for a database, called a schema or a contract

# Basic rule: Do not put the same string data in twice - use a relationship instead

# When there is only one thing in the real world, there should only be one copy of that thing in the database

# Try to model the real world as much as possible

# For each piece for information think about the following: 
#   Is the column an object or an attribute of another object?
#   Once we define objects, we need to define the relationships between the objects
#   What is the thing that is most essential to this application?

# Representing a datamodel in pictures

# Representing a data model in tables

# Primary key is the ending point of the arrow (id), foreign key is the starting point (album_id)

# Logical key: for example, we look up tracks using a logical key that refers to it's title, and the same for an album

# Create the ends of the arrows before you create the beginning of the arrows
