# -*- coding: utf-8 -*-
"""
Created on Mon May 21 13:30:27 2018

@author: Karan
"""

def check_at(x):
    if x.count('@')==1:
        return True
    else:
        return False

def check_dot(x):
    s = x[x.find('@')+1:]
    if s.count('.')==1:
        return True
    else:
        return False

def check_username(x):
    s = x[:x.find('@')]
    flag = False
    for i in s:
        if i.isalnum() or i=='-' or i=='_':
            flag = True
        else: 
            return False
    return flag

def check_website(x):
    s = x[x.find('@')+1:x.find('.')]
    flag = False
    for i in s:
        if i.isalnum():
            flag = True
        else:
            return False
    return flag

def check_extension(x):
    st = x[x.find('.')+1:]
    if len(st)>3:
        return False
    else:
        return True
    
#main script
ip_lst = []
while True:
    ip = raw_input("Enter email address: ")
    if not ip:
        break
    ip_lst.append(ip)

for i in ip_lst:
    if all([check_at(i) and check_dot(i), check_username(i), check_website(i), check_extension(i)]):
        print i


    