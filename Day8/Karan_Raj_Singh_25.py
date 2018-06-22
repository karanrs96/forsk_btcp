# -*- coding: utf-8 -*-
"""
Created on Mon May 21 10:46:53 2018

@author: Karan
"""

lst = []

while True:
    ip = raw_input("Enter name, age & score: ")
    #if ip == "":
    if not ip:
        break
    name, age, score = ip.split(',')
    lst.append((name, int(age), int(score)))

lst.sort()

print lst