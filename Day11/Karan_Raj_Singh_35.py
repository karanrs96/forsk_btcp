# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:05:16 2018

@author: Karan
"""

import pandas as pd

train = pd.read_csv("training_titanic.csv")

print train["Survived"].value_counts()

print train["Survived"].value_counts(normalize = True)

train_sex = train.groupby(["Sex"])

print train_sex["Survived"].value_counts()

print train_sex["Survived"].value_counts(normalize = True)