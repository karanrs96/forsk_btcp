# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:22:12 2018

@author: Karan
"""

import pandas as pd

train = pd.read_csv("training_titanic.csv")

train = train.fillna(train["Age"].mean())

train["Child"] = 0
train["Child"][train["Age"] < 18] = 1

"""
train_grt_age = train[train["Age"] >= 18]
train_lss_age = train[train["Age"] < 18]

train_grt_age["Child"] = 0
train_lss_age["Child"] = 1
"""

train_child =  train.groupby(["Child"])

print train_child["Survived"].value_counts()

print train_child["Survived"].value_counts(normalize = True)
