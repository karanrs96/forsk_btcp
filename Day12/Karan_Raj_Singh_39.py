# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:03:32 2018

@author: Karan
"""

import numpy as np

"""
array = np.array([], np.int64)
i = 0
while i < 40:
    array = np.append(array, int(np.random.uniform(5, 15)))
    i += 1
"""

array = np.random.randint(5,15,size=40)

#with numpy
count = np.bincount(array)
print "With Numpy:", np.argmax(count)

#without numpy
max_dict = {}
for i in array:
    if i not in max_dict:
        max_dict[i] = 1
    else:
        max_dict[i] += 1

maximum = max(max_dict.values())

for i, j in max_dict.items():
    if j == maximum:
        print "Without Numpy:", i
        break