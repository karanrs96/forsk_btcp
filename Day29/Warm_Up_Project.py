# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:21:12 2018

@author: Karan
"""

#scrapping of data
cities = ['gurgaon', 'ghaziabad', 'noida', 'faridabad', 'meerut', 'chandigarh', 'delhi']    #cities near Delhi
#cities = ['gurgaon', 'ghaziabad', 'muzaffarnagar', 'faridabad', 'meerut', 'alwar', 'bharatpur','karnal', 'delhi']

import pandas as pd
df = pd.DataFrame()

import datetime
current_date = datetime.date.today()

import requests
from bs4 import BeautifulSoup

import re

for city in cities:
    temp = []
    wind = []
    humidity = []
    for day in range(0, 6):
        url_day = (current_date + datetime.timedelta(days=day)).strftime ("%Y%m%d")
        url = "https://www.timeanddate.com/weather/india/"+city+"/hourly?hd="+url_day
        
        page = requests.get(url)
            
        bs = BeautifulSoup(page.text, 'html.parser')
        
        table = bs.find('table', class_='zebra tb-wt fw va-m tb-hover')
        
        tbody = table.find('tbody')
        
        table_row = tbody.find_all('tr')
              
        for row in table_row:
            cell = row.find_all('td')
            temp.append(re.sub("[^0-9]", " ", cell[1].text.encode('utf-8')).strip())
            wind.append(re.sub("[^0-9]", " ", cell[4].text.encode('utf-8')).strip())
            humidity.append(re.sub("[^0-9]", " ", cell[6].text.encode('utf-8')).strip())
    
    df['Temperature of '+city] = temp
    df['Wind in '+city] = wind
    df['Humidty in '+city] = humidity
    
df = df.astype(int)
df.to_csv('Weather Details of Next 5 Days.csv', index=False)

#use of regression algorithm

df = pd.read_csv('Weather Details of Next 5 Days.csv')
iv = df.iloc[:, 0:-3].values
dv = df.iloc[:, -3:].values

from sklearn.preprocessing import PolynomialFeatures
poly_obj = PolynomialFeatures(degree = 4)
iv_poly = poly_obj.fit_transform(iv)

from sklearn.model_selection import train_test_split
iv_train, iv_test, dv_train, dv_test = train_test_split(iv_poly, dv, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(iv_train, dv_train)

dv_predict = regressor.predict(iv_test)

from sklearn.model_selection import cross_val_score
accuracy = cross_val_score(estimator = regressor, X = iv_train, y = dv_train, cv = 10)
print "Score using cross validation:", accuracy.mean()