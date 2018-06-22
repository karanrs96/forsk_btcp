# -*- coding: utf-8 -*-
"""
Created on Thu May 17 13:29:42 2018

@author: Karan
"""

import requests

data = {'Phone_Number':'9999999999', 'Name':'Forsk_Hacker', 'College_Name':'Forsk', 'Branch':'ML'}

send_url = "http://13.127.155.43/api_v0.1/sending"
send_req = requests.post(send_url, json = data)
print send_req.text

receive_url = "http://13.127.155.43/api_v0.1/receiving?Phone_Number=9999999999"
receive_req = requests.get(receive_url)
print receive_req.text