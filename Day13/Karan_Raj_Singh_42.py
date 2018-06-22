# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:38:04 2018

@author: Karan
"""

import urllib2
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"

page = urllib2.urlopen(url)

bs = BeautifulSoup(page)

table = bs.find('table', class_='wikitable')

state = []
share = []

for row in table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 7:
        state.append(str(cells[1].text.strip()))
        share.append(str(cells[4].text.strip()))

import pandas as pd

df = pd.DataFrame()

df['State\Territory'] = state
df['National Share(%)'] = share

df = df.iloc[:6,]

import matplotlib.pyplot as plt

plt.rcdefaults()
labels = df["State\Territory"]
explode = [0.2,0,0,0,0,0]
sizes = df["National Share(%)"]
plt.pie(sizes, explode, labels=labels, autopct='%1.2f%%')
plt.show()