# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:30:12 2018

@author: Karan
"""

import facebook as fb

access_token = "EAACEdEose0cBANOifBxypctCUZAlc5SQiqxG1YosLWFTuEijDyZB3fQ2dZCoRXt2BdDCxgbUMlChyRuiydszrXLKgqRYEE37ImOPhFqpcTDCqM7pgjMWrCBKIIf3fEUgMxFXpuftM8ZCOYx3HX3B0hUHzR4mtfPvFy8us6BleTQrybmrkuz7U7Bj2Y6bKhVmWzx0pYr0ZBgZDZD"

status = "Testing Status by Developer"

graph = fb.GraphAPI(access_token)

graph.put_wall_post(status)

graph.put_photo(image=open('sample1.png', 'rb'))