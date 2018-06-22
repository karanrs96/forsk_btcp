# -*- coding: utf-8 -*-
"""
Created on Thu Jun 07 11:14:40 2018

@author: Karan
"""

import pandas as pd

mush = pd.read_csv("mushrooms.csv")

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

for i in range(0, mush.shape[1]):
    mush.iloc[:,i] = le.fit_transform(mush.iloc[:,i])
    
iv = mush.iloc[:, [5,-2,-1]].values
dv = mush.iloc[:, 0].values

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features=[0])
iv = ohe.fit_transform(iv).toarray()
iv = iv[:, 1:]

ohe = OneHotEncoder(categorical_features=[8])
iv = ohe.fit_transform(iv).toarray()
iv = iv[:, 1:]

ohe = OneHotEncoder(categorical_features=[13])
iv = ohe.fit_transform(iv).toarray()
iv = iv[:, 1:]

from sklearn.model_selection import train_test_split
iv_train, iv_test, dv_train, dv_test = train_test_split(iv, dv, test_size=0.25, random_state=0)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5, p=2)
classifier.fit(iv_train, dv_train)

predicted_values = classifier.predict(iv_test)

print "Score:", classifier.score(iv_test, dv_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(dv_test, predicted_values)

