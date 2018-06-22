# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:54:22 2018

@author: Karan
"""

import pandas as pd

dataset = pd.read_csv("Cars.csv")

dataset = dataset.dropna()

dv = dataset["Price"]
iv = dataset.iloc[:, 1:]
#col=list(dataset.columns)
#iv = dataset.iloc[:, 1:].values
#df = pd.DataFrame(dv_train, columns=col[1:])

from sklearn.model_selection import train_test_split

dv_train, dv_test, iv_train, iv_test = train_test_split(dv, iv, random_state=0)

print dv_train
print dv_test
print iv_train
print iv_test

dv_train.to_csv('dv_train.csv', index=False)
dv_test.to_csv('dv_test.csv', index=False)
iv_train.to_csv('iv_train.csv', index=False)
iv_test.to_csv('iv_test.csv', index=False)