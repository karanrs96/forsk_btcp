# -*- coding: utf-8 -*-
"""
Created on Mon May 28 23:10:59 2018

@author: Karan
"""

import requests

pn = raw_input("Enter phone no.: ")
message = raw_input("Enter your message: ")

#api = "http://sms.dataoxytech.com/index.php/smsapi/httpapi/?uname=sylvester007&password=forskmnit&sender=FORSKT&receiver="+pn+"&route=TA&msgtype=1&sms="+message
#api = "http://sms.dataoxytech.com/index.php/smsapi/httpapi/?uname=karanrs96&password=karan@1996&receiver=9680455964&route=PA&msgtype=1&sender=default&sms=testing"
api = "https://smsapi.engineeringtgr.com/send/?Mobile=8562030963&Password=123456789&Key=peeyuHdxN6WbgO4yVQD7u&Message="+message+"&To="+pn
response = requests.post(url=api)

print response