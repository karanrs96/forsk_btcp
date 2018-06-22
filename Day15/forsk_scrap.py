# -*- coding: utf-8 -*-
"""
Created on Wed May 30 10:09:52 2018

@author: Karan
"""

from selenium import webdriver

"""
#fp = webdriver.FirefoxProfile("C:\Users\Karan\AppData\Local\Mozilla\Firefox\Profiles\cw03696s.default")
#browser = webdriver.Firefox(fp,executable_path="C:\\Users\\Karan\\Downloads\\geckodriver\\geckodriver.exe")   #need geckodriver
browser = webdriver.Firefox(executable_path="C:\\Users\\Karan\\Downloads\\geckodriver\\geckodriver.exe")   #need geckodriver
browser.get(url)
"""

url = raw_input("Enter url to scrap code: ")
cp = webdriver.ChromeOptions()
cp.add_argument("user-data-dir=C:\\Users\\Karan\\AppData\\Local\\Google\\Chrome\\User Data")
browser = webdriver.Chrome(executable_path="C:\\Users\\Karan\\Downloads\\chromedriver\\chromedriver.exe", chrome_options=cp)
browser.get(url)

from bs4 import BeautifulSoup

bs = BeautifulSoup(browser.page_source, 'lxml')

text_area = bs.find(class_='vert-mod')

code_area = text_area.find('pre')

f = open('Code.py', 'w')
f.write(code_area.text)
f.close()

"""
f = open('test1.txt', 'w')
f.write(bs.prettify().encode('utf-8'))
f.close()
"""
