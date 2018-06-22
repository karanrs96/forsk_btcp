# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:32:16 2018

@author: Karan
"""

from collections import OrderedDict

dict1 = OrderedDict()

while True:
    ip = raw_input("Enter item name & its price: ")
    if not ip:
        break
    ip_lst = ip.split(" ")
    """
    i = 0
    new_lst = []
    while i < len(ip_lst)-1:
        new_lst.append(ip_lst[i])
        i += 1
    item_name = " ".join(new_lst)
    """
    item_name = " ".join(ip_lst[0:-1])
    price = int(ip_lst[-1])
    if item_name not in dict1.keys():
        dict1[item_name] = price
    else:
        dict1[item_name] = dict1[item_name] + price
    
for i, j in dict1.items():
    print i, j