# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 11:35:36 2018

@author: Karan
"""

import pandas as pd

addhealth = pd.read_csv("tree_addhealth.csv")

#Section 1
iv = addhealth.iloc[:,[0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15]]
dv = addhealth.iloc[:, 7]

most_freq = iv.mode()

for i in range(0, iv.shape[1]):
    iv.iloc[:, i] = iv.iloc[:, i].fillna(most_freq.iloc[0, i])
    
from sklearn.model_selection import train_test_split
iv_train, iv_test, dv_train, dv_test = train_test_split(iv, dv, test_size=0.2, random_state=0)

from sklearn.tree import DecisionTreeClassifier
classifier1 = DecisionTreeClassifier(criterion='entropy', random_state=0)
classifier1.fit(iv_train, dv_train)

predicted = classifier1.predict(iv_test)

print "Score for Section 1:", classifier1.score(iv_test, dv_test)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(dv_test, predicted)

print "Confusion matrix for Section 1:\n", cm

#Section 2
iv = addhealth.iloc[:,[0, 16]]
dv = addhealth.iloc[:, 21]

most_freq = iv.mode()

for i in range(0, iv.shape[1]):
    iv.iloc[:, i] = iv.iloc[:, i].fillna(most_freq.iloc[0, i])

mf = dv.mode()

dv = dv.fillna(mf[0])
  
iv_train, iv_test, dv_train, dv_test = train_test_split(iv, dv, test_size=0.2, random_state=0)

classifier2 = DecisionTreeClassifier(criterion='entropy', random_state=0)
classifier2.fit(iv_train, dv_train)

predicted = classifier2.predict(iv_test)

print "Score for Section 2:", classifier2.score(iv_test, dv_test)

cm = confusion_matrix(dv_test, predicted)

print "Confusion matrix for Section 2:\n", cm

#Section 3
iv = addhealth.iloc[:, 1:6]
dv = addhealth.iloc[:, 7]

iv_train, iv_test, dv_train, dv_test = train_test_split(iv, dv, test_size=0.2, random_state=0)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion='entropy', random_state=0)
classifier.fit(iv_train, dv_train)

predicted = classifier.predict(iv_test)

print "Score for Section 3:", classifier.score(iv_test, dv_test)

cm = confusion_matrix(dv_test, predicted)

print "Confusion matrix for Section 3:\n", cm