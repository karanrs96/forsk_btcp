# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 11:42:49 2018

@author: Karan
"""

from havenondemand.hodclient import *
import json
import pandas as pd

client = HODClient("16624cb2-cf84-4887-8463-cc7aba87a357", "v1") #apikey

#params = {'url': 'https://www.havenondemand.com/sample-content/videos/gb-plates.mp4', 'source_location': 'GB'} ##if using url
#params = {'file': 'gb-plates.mp4', 'source_location': 'GB'} ## or if using a local file
params = {'file': 'car_plate.mp4', 'source_location': 'IN'} ## or if using a local file
response_async = client.post_request(params, 'recognizelicenseplates', async=True)
jobID = response_async['jobID']
#print jobID

## Wait some time afterwards for async call to process...
response = client.get_job_result(jobID)
print response

#dump data in a json file
with open('data.json', 'w') as outfile:
    json.dump(response, outfile)