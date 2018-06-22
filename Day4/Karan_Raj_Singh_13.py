# -*- coding: utf-8 -*-
"""
Created on Tue May 15 12:08:01 2018

@author: Karan
"""

def pattern(n):
    i = 0
    while i < n:
        j = i + 1
        print j*'*',
        print
        i = i + 1
    while i > 1:
        j = i - 1
        print j*'*',
        print
        i = i - 1

#main script
num = input("Enter value of n: ")
pattern(num)