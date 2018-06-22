# -*- coding: utf-8 -*-
"""
Created on Mon May 14 22:20:40 2018

@author: Karan
"""

def Print():
    print "Sum =", Add(list1)
    print "Multiply =", Multiply(list1)
    print "Largest =", Largest(list1)
    print "Smallest =", Smallest(list1)
    print "Sorted =", Sorting(list1)
    print "Without Duplicates =", Remove_Duplicates(list1)
    
def Add(local_list):
    """
    Sum = 0
    for i in local_list:
        Sum = Sum + i
    """
    return sum(local_list)

def Multiply(local_list):
    """
    Mul = 1
    for i in local_list:
        Mul = Mul * i
    """
    return reduce(lambda x,y : x*y, local_list)

def Largest(local_list):
    return max(local_list)

def Smallest(local_list):
    return min(local_list)

def Sorting(local_list):
    local_list.sort()
    return local_list

def Remove_Duplicates(local_list):
    """
    local_list.sort()
    new_list = []
    i = 0
    while i < len(local_list):
        if i == len(local_list)-1:
            new_list.append(local_list[i])
            break
        if local_list[i] == local_list[i+1]:
            i = i + 1
        else:
            new_list.append(local_list[i])
            i = i + 1
    return new_list
    """
    new_list = list(set(local_list))
    return new_list
    
#main script
ip = input("Enter a list of numbers: ")  #must be in form "1,2,3,.."
list1 = list(ip)  
Print()