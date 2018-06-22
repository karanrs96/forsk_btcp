# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:12:28 2018

@author: Karan
"""

#finding mean of given numbers while ignoring one copy of largest & smallest

#input must be in form "1,2,3,4"
ipstr = raw_input("Enter list of numbers: ")

list1 = ipstr.split(',')

i = 0
while i < len(list1):
    list1[i] = int(list1[i])
    i += 1

"""    
smallest = list1[0]
largest = 0

for i in list1:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
"""

smallest = min(list1)
largest = max(list1)

summ = 0        
for i in list1:
  summ += i

avg = (summ-smallest-largest)/(len(list1)-2)  

print avg