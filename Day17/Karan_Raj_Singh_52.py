# -*- coding: utf-8 -*-
"""
Created on Fri Jun 01 11:35:59 2018

@author: Karan
"""

import pandas as pd
import numpy as np

iq = pd.read_csv("iq_size.csv")

iv = iq.iloc[:, 1:].values
dv = iq.iloc[:, 0:1].values

"""
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
iv = sc.fit_transform(iv)
"""

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(iv, dv)

print "Prediction of 90, 70 & 150:", lr.predict(np.array([90, 70, 150]).reshape(1, -1))
#print lr.predict(iv[2, :].reshape(1, -1))
print "Score:", lr.score(iv, dv)

import statsmodels.formula.api as sm
iv = np.append(arr=np.ones((38, 1)).astype(int), values=iv, axis=1)

iv_opt = iv[:, [0, 1, 2, 3]]
regressor_ols = sm.OLS(endog=dv,exog=iv_opt).fit()
regressor_ols.summary()

iv_opt = iv[:, [0, 1, 2]]
regressor_ols = sm.OLS(endog=dv,exog=iv_opt).fit()
regressor_ols.summary()

iv_opt = iv[:, [1, 2]]
regressor_ols = sm.OLS(endog=dv,exog=iv_opt).fit()
regressor_ols.summary()

iv_opt = iv[:, [1]]
regressor_ols = sm.OLS(endog=dv,exog=iv_opt).fit()
regressor_ols.summary()