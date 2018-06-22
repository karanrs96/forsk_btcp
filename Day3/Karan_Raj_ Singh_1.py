# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:38:24 2018

@author: Karan
"""

#converting user input like "1,2,3,4" into list & tuple
ipstr = raw_input("Enter list of string: ")

list1 = ipstr.split(',');

tuple1 = tuple(list1)

print list1
print tuple1