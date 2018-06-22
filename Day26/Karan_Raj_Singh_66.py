# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 12:38:44 2018

@author: Karan
"""

import pandas as pd

dataset = pd.read_csv("banknotes.csv")

iv = dataset.iloc[:,1:-1]
dv = dataset.iloc[:, -1]

from sklearn.model_selection import train_test_split
iv_train, iv_test, dv_train, dv_test = train_test_split(iv, dv, test_size=0.2, random_state=0)

"""
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion='entropy', random_state=0)
classifier.fit(iv_train, dv_train)
"""

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(iv_train, dv_train)

dv_predict = classifier.predict(iv_test)

print classifier.score(iv_test, dv_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(dv_test, dv_predict)
print "Confusion Matrix:\n", cm

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = iv_test, y = dv_test, cv = 10)
print accuracies.mean()