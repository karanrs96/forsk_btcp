# -*- coding: utf-8 -*-
"""
Created on Wed Jun 06 11:05:01 2018

@author: Karan
"""

import pandas as pd

aff = pd.read_csv("affairs.csv")

iv = aff.iloc[:, :-1]
dv = aff.iloc[:, -1]

iv = pd.get_dummies(iv, columns=["occupation"])
iv = iv.iloc[:,:-1]
iv = pd.get_dummies(iv, columns=["occupation_husb"])
iv = iv.iloc[:,:-1]

from sklearn.model_selection import train_test_split
iv_train, iv_test, dv_train, dv_test = train_test_split(iv, dv, test_size=0.2, random_state=0)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(iv_train, dv_train)
predict = pd.Series(classifier.predict(iv_test))

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(dv_test, predict)
total = float(cm[0,0] + cm[0,1] + cm[1,0] + cm[1,1])
correct = float(cm[0,0]+cm[1,1])
print "Score using Confusion Matrix:", correct/total

print "Score using .score():", classifier.score(iv_test, dv_test)

#print "% of women actually had affair:", float(cm[0,1]+cm[1,1])/total
print "% of women actually had affair:", predict.value_counts(normalize=True).iloc[1]

import numpy as np
print "Prediction of given woman:", classifier.predict(np.array([3, 25, 3, 1, 4, 16, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]).reshape(1, -1))

#building optimum model
import statsmodels.formula.api as sm
iv = aff.iloc[:, :-1]
iv = np.append(arr=np.ones((6366, 1)).astype(int), values=iv, axis=1)

iv_opt = iv[:, [0,1,2,3,4,5,6,7,8]]
ols = sm.OLS(endog=dv, exog=iv_opt).fit()
ols.summary()

iv_opt = iv[:, [0,1,2,3,5,6,7,8]]
ols = sm.OLS(endog=dv, exog=iv_opt).fit()
ols.summary()

iv_opt = iv[:, [0,1,2,3,5,6,7]]
ols = sm.OLS(endog=dv, exog=iv_opt).fit()
ols.summary()