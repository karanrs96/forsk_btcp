# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 11:11:17 2018

@author: Karan
"""

import pandas as pd

dataset = pd.read_csv("movie.csv")

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

relevant = []

for i in range(0, dataset.shape[0]):
    text = re.sub('[^a-zA-Z]', ' ', dataset['text'][i])
    text = text.lower()
    text = text.split()
    ps = PorterStemmer()
    text = [ps.stem(word) for word in text if not word in set(stopwords.words('english'))]
    text = ' '.join(text)
    relevant.append(text)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1000)
iv = cv.fit_transform(relevant).toarray()
#dv = dataset.iloc[:,0].astype('category').cat.codes.values
dv = dataset.iloc[:,0]

from sklearn.model_selection import train_test_split
iv_train, iv_test, dv_train, dv_test = train_test_split(iv, dv, test_size=0.2, random_state=0)

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(iv_train, dv_train)

dv_predict = classifier.predict(iv_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(dv_test, dv_predict)