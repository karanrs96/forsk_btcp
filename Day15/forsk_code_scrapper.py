# -*- coding: utf-8 -*-
"""
Created on Wed May 30 18:03:13 2018

@author: Karan
"""

f = open('page source.txt', 'r')
page_source = f.read()
f.close()

from bs4 import BeautifulSoup

bs = BeautifulSoup(page_source, 'lxml')

blue_block = bs.find('div', class_="seq_contents tex2jax_ignore asciimath2jax_ignore")

bs = BeautifulSoup(blue_block.text, 'lxml')

text_area = bs.find(class_='vert-mod')

code_area = text_area.find('pre')

f = open('Code.py', 'w')
f.write(code_area.text)
f.close()

"""
f = open('test.txt', 'w')
f.write(code_area.prettify(encoding='utf-8'))
f.close()
"""