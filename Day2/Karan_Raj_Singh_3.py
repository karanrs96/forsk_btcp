# -*- coding: utf-8 -*-
"""
Created on Fri May 11 11:29:27 2018

@author: Karan
"""

str1 = raw_input("Enter a string: ")

"""
str2=""

for i in str1:
    i = i + "*"
    str2 = str2 + i

print str2
"""
str2 = "*".join(str1)

print str2