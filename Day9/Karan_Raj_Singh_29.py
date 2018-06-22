# -*- coding: utf-8 -*-
"""
Created on Tue May 22 11:55:09 2018

@author: Karan
"""

import re

ip_lst = []
while True:
    ip = raw_input("Enter floating point number: ")
    if not ip:
        break
    ip_lst.append(ip)
   
for i in ip_lst:  
    #if re.match(r'[+-]?[0-9]*\.[0-9]+$', i) == None:
    if re.match(r'(\+{0,1}|\-{0,1})\d*\.\d+$', i) == None:
        print False
    else:
        print True