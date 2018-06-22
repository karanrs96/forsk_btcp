# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:20:06 2018

@author: Karan
"""

import pandas as pd

dataset = pd.read_csv("breast_cancer.csv")

iv = dataset.iloc[:, 1:-1]
dv = dataset.iloc[:, -1]

most_freq = iv.mode()

for i in range(0, iv.shape[1]):
    iv.iloc[:,i] = iv.iloc[:,i].fillna(most_freq.iloc[0,i])
    
from sklearn.model_selection import train_test_split
iv_train, iv_test, dv_train, dv_test = train_test_split(iv, dv, test_size=0.2, random_state=0)

from sklearn.svm import SVC
classifier = SVC(kernel='linear', random_state=0)
classifier.fit(iv_train, dv_train)

dv_predict = classifier.predict(iv_test)

print "Score:", classifier.score(iv_test, dv_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(dv_test, dv_predict)

print "Confusion Matrix:\n", cm

print "Prediction of given data set:", classifier.predict([[6, 2, 5, 3, 2, 7, 9, 2, 4]])