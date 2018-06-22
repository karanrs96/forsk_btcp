# -*- coding: utf-8 -*-
"""
Created on Tue May 22 17:23:19 2018

@author: Karan
"""

import re

ip_lst = []

while True:
    ip = raw_input("Enter a email address: ")
    if not ip:
        break
    ip_lst.append(ip)
  
op_lst = []
    
for i in ip_lst:
    if re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.\w{2,4}', i):
        op_lst.append(i)
    
op_lst.sort()

print op_lst