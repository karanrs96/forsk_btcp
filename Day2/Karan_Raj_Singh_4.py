# -*- coding: utf-8 -*-
"""
Created on Fri May 11 11:21:07 2018

@author: Karan
"""

str1 = raw_input("Enter your full name: ")

"""
lst = str1.split(" ")

lst.reverse()

str2 = " ".join(lst)

print str2
"""
str2 = str1.strip()

i = str2.index(" ")

str3 = str2[0:i].strip()
str4 = str2[i+1:].strip()

print str4, str3
