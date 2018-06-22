# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:02:35 2018

@author: Karan
"""

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/rasbt/pattern_classification/master/data/wine_data.csv', usecols=[0,1,2], header=None, names=['Class label', 'Alcohol', 'Malic Acid'])

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

df1 = sc.fit_transform(df)

from sklearn.preprocessing import MinMaxScaler

mmsc = MinMaxScaler()

df2 = mmsc.fit_transform(df)