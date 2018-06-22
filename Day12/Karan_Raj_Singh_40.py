# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:51:30 2018

@author: Karan
"""

import numpy as np

ip = raw_input("Enter 9 space seperated numbers: ")
ip_lst = ip.split(" ")

"""
array = np.array([], np.int64)

for i in ip_lst:
    array = np.append(array, int(i))
"""

array = np.array(ip_lst, np.int64)
array = array.reshape(3,3)

print array