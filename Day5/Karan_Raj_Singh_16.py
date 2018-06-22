# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:37:07 2018

@author: Karan
"""

vowels = "AaEeIiOoUu "

ipstr = raw_input("Enter a string: ")

list1 = list(ipstr)

i = 0
while i < len(list1):
    if list1[i] in vowels:
        i = i + 1
    else:
        list1.insert(i+1, 'o'+list1[i])
        i = i + 2
        
newstr = ''.join(list1)

print newstr