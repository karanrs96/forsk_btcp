# -*- coding: utf-8 -*-
"""
Created on Thu May 17 11:48:49 2018

@author: Karan
"""

def print_rev(st):
    """
    st_list = []
    i = -1
    limit = -(len(st))
    while i >= limit:
        st_list.append(st[i])
        i = i-1
    new_st = "".join(st_list)
    return new_st
    """
    return ipstr[::-1]

#main script
    
ipstr = raw_input("Enter a string: ")
print print_rev(ipstr)