# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:59:30 2018

@author: Karan
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(150, 20, 1000)

plt.hist(data, 100)
plt.show()

print np.std(data)
print np.var(data)