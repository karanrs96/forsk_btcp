# -*- coding: utf-8 -*-
"""
Created on Fri Jun 01 12:24:01 2018

@author: Karan
"""

import pandas as pd
import numpy as np

ht = pd.read_csv("stats_females.csv")

iv = ht.iloc[:, 1:].values
dv = ht.iloc[:, 0:1].values

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(iv, dv)

import statsmodels.formula.api as sm
iv = np.append(arr=np.ones((214, 1)).astype(int), values=iv, axis=1)

iv_opt = iv[:, [0, 1, 2]]
regressor_ols = sm.OLS(endog=dv, exog=iv_opt).fit()
regressor_ols.summary()

print "Both I.V. are significant for Student's Height"

print "Mother's Height Coefficient:", regressor_ols.params[1]
print "Father's Height Coefficient:", regressor_ols.params[2]