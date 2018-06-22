# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:08:24 2018

@author: Karan
"""

import pandas as pd
import numpy as np

am = pd.read_csv("Automobile.csv")

am["price"] = am["price"].fillna(am["price"].mean())

array = np.array(am["price"])

print "Min Price:", np.min(array)
print "Max Price:", np.max(array)
print "Avg Price:", np.mean(array)
print "Standard Deviation of Price:", np.std(array)