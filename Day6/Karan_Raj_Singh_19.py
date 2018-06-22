# -*- coding: utf-8 -*-
"""
Created on Thu May 17 11:09:31 2018

@author: Karan
"""
#import string

def pangram(st):
    ipstr_set = set(st)
    count = 0
    for i in ipstr_set:
        if 'a' <= i <= 'z':
            count = count + 1       
    if count == 26:
        return "PANAGRAM"
    else:
        return "NOT PANAGRAM"

"""    
def pangram(st):
    alpha_dict = {}
    for i in string.ascii_lowercase:
        alpha_dict[i]=False
    for i in st:
        if i in alpha_dict.keys():
            alpha_dict[i] = True
    for i in alpha_dict.keys():
        if alpha_dict[i] == False:
            return "NOT PANGRAM"
    return "PANGRAM"
"""

#main script
ipstr = raw_input("Enter a string: ")
print pangram(ipstr.lower())