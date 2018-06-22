# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:31:53 2018

@author: Karan
"""
#returning sum of numbers except 13 and number right after 13 in a list

#input must be in form "1,2,3,4"
ipstr = raw_input("Enter list of numbers: ")

list1 = ipstr.split(',')

i = 0
while i < len(list1):
    list1[i] = int(list1[i])
    i += 1
    
summ = 0
i = 0
while i < len(list1):
    if list1[i] == 13 or list1[i-1] == 13:
        i += 1
        continue
    else:
        summ += list1[i]
    i += 1
    
print summ