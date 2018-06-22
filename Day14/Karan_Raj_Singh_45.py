# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:08:51 2018

@author: Karan
"""

import pandas as pd

am = pd.read_csv("Automobile.csv")

#print am.dtypes

df = pd.DataFrame(am).select_dtypes(include=[object])
str_col_name = list(df)

#print df

numeric_df = pd.DataFrame(am).select_dtypes(exclude=[object])

num_col_names = list(numeric_df)

from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)
imputer = imputer.fit(am[num_col_names])
am[num_col_names] = imputer.transform(am[num_col_names])

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder = LabelEncoder()
for i in str_col_name:
    am[i] = labelencoder.fit_transform(am[i])

onehotencoding = OneHotEncoder(categorical_features=[6,7])
am = onehotencoding.fit_transform(am).toarray()