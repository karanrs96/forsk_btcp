# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:11:05 2018

@author: Karan
"""

import pandas as pd

am = pd.read_csv("Automobile.csv")

am_makers = am.groupby(["make"])

df = am["make"].value_counts()

df = pd.DataFrame({'make': df.index, 'count' : df.values})

import matplotlib.pyplot as plt

max_count = max(df.iloc[0:10, 0])

exp = []
for i in df.iloc[0:10, 0]:
    if i == max_count:
        exp.append(.2)
    else:
        exp.append(0)

plt.pie(df.iloc[0:10, 0], labels=df.iloc[0:10, 1], explode=exp, autopct="%1.2f%%")
plt.show()