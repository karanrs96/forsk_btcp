# -*- coding: utf-8 -*-
"""
Created on Tue May 22 18:05:59 2018

@author: Karan
"""

import re

ip_lst = []

while True:
    ip = raw_input("Enter credit card number: ")
    if not ip:
        break
    ip_lst.append(ip)

regex = re.compile(r'[4-6][0-9]{15}|([4-6][0-9]{3}(-[0-9]{4}){3})')

for i in ip_lst:
    if regex.match(i):
        print "Valid"
    else:
        print "Invalid"