# -*- coding: utf-8 -*-
"""
Created on Fri May 18 11:18:42 2018

@author: Karan
"""

import urllib2
import json
import oauth2
import time

search_str = raw_input("Enter search string: ")

api_url = "https://api.twitter.com/1.1/search/tweets.json"

para = {"oauth_version" : "1.0", "oauth_nonce": oauth2.generate_nonce(), "oauth_timestamp":int(time.time())}

api_key = "Rrr8Lvpx6PHy5TRULGk6Id7Bm"
api_secret = "GFvgXdZXBbCouOF0rIiL4XyQ3qIZ9ZjRZCTlVqtvubgrHTf821" 
token_key = "997356131205894145-SmSE2QcYhjF8vnQ2CKiOxsEUSFKTK05"
token_secret = "acGJEgxyih5pS38Gw1FLtbkyTljme18LD8RlegtXhTYii" 

consumer = oauth2.Consumer(key=api_key, secret=api_secret)
token = oauth2.Token(key=token_key, secret=token_secret)

para["oauth_consumer"] = consumer.key
para["oauth_token"] = token.key
para["q"] = search_str

req = oauth2.Request(method="GET", url=api_url, parameters=para)

signature_method = oauth2.SignatureMethod_HMAC_SHA1()
req.sign_request(signature_method, consumer, token)
url = req.to_url()
response = urllib2.Request(url)
data = json.load(urllib2.urlopen(response))

filename = para["q"]
f = open(filename+"_File.txt", "w")
json.dump(data["statuses"], f)
f.close()