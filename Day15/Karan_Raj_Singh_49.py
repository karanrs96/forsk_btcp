# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:31:34 2018

@author: Karan
"""

import pandas as pd
import numpy as np

df = pd.read_csv("Red_Wine.csv")

df.iloc[:, 0] = df.iloc[:, 0].fillna(df.iloc[:, 0].value_counts().index[0])
df = df.fillna(np.mean(df))

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
df.iloc[:,0] = labelencoder.fit_transform(df.iloc[:,0])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features=[0])
df = onehotencoder.fit_transform(df).toarray()

iv = df[:, :-1]
dv = df[:, -1]

from sklearn.model_selection import train_test_split
iv_train, iv_test, dv_train, dv_test = train_test_split(iv, dv, test_size=0.2, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
iv_train = sc.fit_transform(iv_train)
iv_test = sc.fit_transform(iv_test)
#dv_train = sc.fit_transform(dv_train.reshape(-1,1))


