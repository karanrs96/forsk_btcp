# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:05:12 2018

@author: Karan
"""

#count letters and digits in a input string

ipstr = raw_input("Enter a string: ")

#list1 = list(ipstr)

letters = 0
digits = 0

for i in ipstr:
    #if '0' <= i <='9':
    if i.isdigit():
        digits += 1
    #elif 'a' <= i <= 'z' or 'A' <= i <= 'Z':
    elif i.isalpha(): 
        letters += 1
        
print "Letters", letters
print "Digits", digits