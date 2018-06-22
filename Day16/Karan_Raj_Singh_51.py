# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:31:45 2018

@author: Karan
"""

import pandas as pd

bvsd = pd.read_csv("Bahubali2_vs_Dangal.csv")

b = bvsd.iloc[:, [0,1]]
d = bvsd.iloc[:, [0,2]]

b_iv = b.iloc[:, 0:1].values
b_dv = b.iloc[:, 1].values

d_iv = d.iloc[:, 0:1].values
d_dv = d.iloc[:, 1].values

"""
from sklearn.model_selection import train_test_split

b_iv_train, b_iv_test, b_dv_train, b_dv_test = train_test_split(b_iv, b_dv, test_size=0.2, random_state=0)
"""

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(b_iv, b_dv)

print "Bahubali 2 Prediction of 10th Day:", lr.predict(10)
print "Score:", lr.score(10,lr.predict(10))

lr.fit(d_iv, d_dv)

print "Dangal Prediction of 10th Day:", lr.predict(10)
print "Score:", lr.score(10,lr.predict(10))