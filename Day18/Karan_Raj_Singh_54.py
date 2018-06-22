# -*- coding: utf-8 -*-
"""
Created on Mon Jun 04 10:15:28 2018

@author: Karan
"""

import pandas as pd

bluegill = pd.read_csv("bluegills.csv")

iv = bluegill.iloc[:, 0:1].values
dv = bluegill.iloc[:, 1].values

from sklearn.linear_model import LinearRegression

lr1 = LinearRegression()
lr1.fit(iv, dv)
print "Linear Regression Score",lr1.score(iv, dv)

import matplotlib.pyplot as plt

plt.scatter(iv, dv, color='red')
plt.plot(iv, lr1.predict(iv), color='blue')
plt.show()

from sklearn.preprocessing import PolynomialFeatures
poly_obj = PolynomialFeatures(degree=4)
iv_poly = poly_obj.fit_transform(iv)

lr2 = LinearRegression()
lr2.fit(iv_poly, dv)
print "Polynomial Regression Score",lr2.score(iv_poly, dv)

print "Polynomial Prediction of Age=5", lr2.predict(poly_obj.fit_transform(5))

plt.scatter(iv, dv, color='red')
plt.plot(iv, lr2.predict(poly_obj.fit_transform(iv)), color='blue')
plt.show()

#for smoother plot
import numpy as np
iv_grid = np.arange(min(iv), max(iv), 0.1)
iv_grid = iv_grid.reshape((-1, 1))
plt.scatter(iv, dv, color = 'red')
plt.plot(iv_grid, lr2.predict(poly_obj.fit_transform(iv_grid)), color = 'blue')