# -*- coding: utf-8 -*-
"""
Created on Thu May 17 11:59:36 2018

@author: Karan
"""

import json
import urllib2

url_s = "http://13.127.155.43/api_v0.1/sending"
url_r = "http://13.127.155.43/api_v0.1/receiving"

values = {'Phone_Number':'9999999999', 'Name':'Forsk_Hacker', 'College_Name':'Forsk', 'Branch':'ML'}

data = json.dumps(values)
header = {"Content-Type":"application/json"}
req = urllib2.Request(url_s, data,headers=header)
response = urllib2.urlopen(req)
print response.read()

req2 = urllib2.Request(url_r+"?Phone_Number=9999999999")
response2 = urllib2.urlopen(req2)
print response2.read()
