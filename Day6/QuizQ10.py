# -*- coding: utf-8 -*-
"""
Created on Thu May 17 16:12:31 2018

@author: Karan
"""
import doctest
def Add(p, q):
    """
Perform Addition
>>> Add(12,3)
15
>>> Add(4,5)
9
    """
    return p*q
doctest.testmod()