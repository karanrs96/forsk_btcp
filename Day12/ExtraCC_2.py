# -*- coding: utf-8 -*-
"""
Created on Tue May 29 17:20:59 2018

@author: Karan
"""

import requests
from bs4 import BeautifulSoup

sign = raw_input("Enter your zodiac sign: ")

page = requests.get("https://www.astrology.com/horoscope/daily/"+sign.lower()+".html")

bs = BeautifulSoup(page.text, 'html.parser')

all_p = bs.find_all('p')

print all_p[0].text