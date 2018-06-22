# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:49:49 2018

@author: Karan
"""

#count number of characters in string

ipstr = raw_input("Enter string: ")

#Kriti ka method
dict1 = {}
for i in ipstr:
    dict1[i] = ipstr.count(i)
    
print dict1