# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:52:51 2018

@author: Karan
"""

import pandas as pd

ft = pd.read_csv("Foodtruck.csv")

iv = ft.iloc[:, 0:1].values
dv = ft.iloc[:, 1].values

from sklearn.model_selection import train_test_split

iv_train, iv_test, dv_train, dv_test = train_test_split(iv, dv, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(iv_train, dv_train)

predicted_values = lr.predict(iv_test)

print "Score:", lr.score(iv_test, dv_test)

print "Prediction for Jaipur:", lr.predict(3.073)

"""
import matplotlib.pyplot as plt

plt.scatter(iv_test, dv_test, color='red') 
plt.plot(iv_train, lr.predict(iv_train), color='blue')
plt.xlabel("Population")
plt.ylabel("Profit")
plt.show()
"""