# -*- coding: utf-8 -*-
"""
Created on Sun Jul 03 13:16:43 2016

@author: Rahul Patni
"""

# Many-to-Many Relationships in SQL

# A book can have many authors and a author can write many books
# In an album, there can be many authors

# Example statement where the first 2 items are primary keys
# INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);

# SQL Statement Example
#SELECT User.name, Member.role, Course.title
#FROM User Join Member JOIN Course
#ON Member.user_id = User.id AND Member.course_id = Course.id
#ORDER BY Course.title, Member.role DESC, User.name