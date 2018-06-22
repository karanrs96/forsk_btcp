# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:54:54 2018

@author: Karan
"""

#count number of characters in string

ipstr = raw_input("Enter character string: ")

list1 = list(ipstr)

dict1 = {}

for i in list1:
    dict1[i] = None
    
for i in list1:
    if dict1[i] == None:
        dict1[i] = 1
    else:
        dict1[i] += 1
        
print dict1