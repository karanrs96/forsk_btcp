# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 11:55:55 2018

@author: Karan
"""

import pandas as pd
f = pd.read_csv("Auto_mpg.txt", delim_whitespace=True, header=None, names=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"])
#f = pd.read_fwf("Auto_mpg.txt", header=None)

import numpy as np
f.iloc[:, 3] = f.iloc[:, 3].replace('?', np.NaN)
f.iloc[:, 3] = pd.to_numeric(f.iloc[:, 3])
f.iloc[:, 3] = f.iloc[:, 3].fillna(np.mean(f.iloc[:, 3]))

"""
from sklearn.preprocessing import Imputer
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
f.iloc[:, 3:4] = imp.fit_transform(f.iloc[:, 3:4])
"""

f_mpg = f.groupby(["mpg"])
print "Car with highest mpg:", f_mpg["car name"].value_counts().index[-1]

iv = f.iloc[:, 1:8].values
dv = f.iloc[:, 0].values

from sklearn.model_selection import train_test_split
iv_train, iv_test, dv_train, dv_test = train_test_split(iv, dv, test_size=0.2, random_state=0)

from sklearn.tree import DecisionTreeRegressor
dtregressor = DecisionTreeRegressor(random_state=0)
dtregressor.fit(iv_train, dv_train)

print "Decision Tree Regression Score:", dtregressor.score(iv_test, dv_test)

from sklearn.ensemble import RandomForestRegressor
rfregressor = RandomForestRegressor(n_estimators=10, random_state=0)
rfregressor.fit(iv_train, dv_train)

print "Random Forest Regression Score:", rfregressor.score(iv_test, dv_test)

print "Decision Tree Prediction:", dtregressor.predict(np.array([6, 215, 100, 2630, 22.2, 80, 3]).reshape(1, -1))

print "Random Forest Prediction:", rfregressor.predict(np.array([6, 215, 100, 2630, 22.2, 80, 3]).reshape(1, -1))