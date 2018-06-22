# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:38:02 2018

@author: Karan
"""
def palindrome(x):
    if x==x[::-1]:
        return True
    else:
        return False
    
def positive(x):
    for i in x:
        if int(i)<0:
            return False
    return True
    
ip = raw_input("Enter space seperated list of integer: ")
ip_lst = ip.split(" ")
    
check_pos = positive(ip_lst)

op_lst = []

for i in ip_lst:
    op_lst.append(check_pos and palindrome(i))
    
print any(op_lst)
 