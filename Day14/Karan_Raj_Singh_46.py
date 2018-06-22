# -*- coding: utf-8 -*-
"""
Created on Tue May 29 13:11:19 2018

@author: Karan
"""

import pandas as pd

loan = pd.read_csv("Loan.csv")

str_col_names = list(pd.DataFrame(loan).select_dtypes(include=[object]))

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

for i in str_col_names:
    loan[i] = labelencoder.fit_transform(loan[i])
    
iv = loan.iloc[:, :-1]
dv = loan.iloc[:, -1]

from sklearn.model_selection import train_test_split

iv_train, iv_test, dv_train, dv_test = train_test_split(iv, dv, test_size=0.2, random_state=0) 

from sklearn.preprocessing import OneHotEncoder

onehotencoder = OneHotEncoder(categorical_features=[-1])
iv_train = onehotencoder.fit_transform(iv_train).toarray()
iv_test = onehotencoder.fit_transform(iv_test).toarray()

"""
from sklearn.preprocessing import LabelEncoder

str_col_names = list(pd.DataFrame(iv_train).select_dtypes(include=[object]))
del str_col_names[0]

labelencoder = LabelEncoder()
for i in str_col_names:
    iv_train[i] = labelencoder.fit_transform(iv_train[i])
    iv_test[i] = labelencoder.fit_transform(iv_test[i])
    
dv_train = labelencoder.fit_transform(dv_train)
dv_test = labelencoder.fit_transform(dv_test)
"""