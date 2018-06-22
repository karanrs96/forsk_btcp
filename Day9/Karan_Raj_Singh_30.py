# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:24:07 2018

@author: Karan
"""

import urllib2
from bs4 import BeautifulSoup

url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

page = urllib2.urlopen(url)

bs = BeautifulSoup(page)

table = bs.find_all('tbody')

pos = []
team = []
matches = []
points = []
ratings = []


tr_table = table[0].find_all('tr')

for row in tr_table:
    
    cells = row.findAll('td')
 
    pos.append(str(cells[0].text.strip()))
    team.append(str(cells[1].text.strip()))
    matches.append(str(cells[2].text.strip()))
    points.append(str(cells[3].text.strip()))
    ratings.append(str(cells[4].text.strip()))
    
import pandas as pd

df = pd.DataFrame()
df['Position'] = pos
df['Team']=team
df['Matches']=matches
df['Points']=points
df['Rating']=ratings

print df

    