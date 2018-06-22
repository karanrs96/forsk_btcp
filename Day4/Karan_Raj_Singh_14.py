# -*- coding: utf-8 -*-
"""
Created on Tue May 15 12:40:54 2018

@author: Karan
"""

def fix_teen(n):
    if n in range(13,20):
        if n==15 or n==16:
            return n
        else:
            return 0
    else:
        return n
        
dict1 = {'a':0, 'b':0, 'c':0}
inp = input("Enter values for a,b,c: ")
j = 0
for i in dict1.keys():
    dict1[i] = inp[j]
    j = j + 1

""" 
Sum = 0
for i in dict1.values():
    Sum = Sum + fix_teen(i)
"""
 
print "Sum =", sum(map(fix_teen, dict1.values()))