# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 11:19:36 2018

@author: Karan
"""

import pandas as pd
ph = pd.read_csv("PastHires.csv")

iv = ph.iloc[:, 0:6].values
dv = ph.iloc[:, 6].values

from sklearn.preprocessing import LabelEncoder
le1 = LabelEncoder()
le2 = LabelEncoder()
iv[:,1] = le1.fit_transform(iv[:,1])
iv[:,3] = le1.fit_transform(iv[:,3])
iv[:,4] = le1.fit_transform(iv[:,4])
iv[:,5] = le1.fit_transform(iv[:,5])
dv = le2.fit_transform(dv)

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(iv, dv)

print "Accuracy of Prediction:", regressor.score(iv, dv)

from sklearn.ensemble import RandomForestRegressor
new_regressor = RandomForestRegressor(n_estimators=10, random_state=0)
new_regressor.fit(iv, dv)

import numpy as np
print new_regressor.predict(np.array([10, 1, 4, 0, 1, 0]).reshape(1, -1))
print new_regressor.predict(np.array([10, 1, 4, 1, 0, 1]).reshape(1, -1))

"""
test1 = np.array([[10, 'Y', 4, 'BS', 'Y', 'N']], dtype=object).reshape(1, -1)
test1[:,1] = le1.transform(test1[:,1])
test1[:,3] = le1.transform(test1[:,3])
test1[:,4] = le1.transform(test1[:,4])
test1[:,5] = le1.transform(test1[:,5])
"""
