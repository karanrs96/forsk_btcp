# -*- coding: utf-8 -*-
"""
Created on Wed May 23 12:33:45 2018

@author: Karan
"""

import json
import urllib2

insert_api = "https://api.mlab.com/api/1/databases/db_university/collections/students?apiKey=cxzVW0OfZ_Nb1DtxpFHiXUdc0ChbyKzX"
   
name = raw_input("Enter student name: ")
age = raw_input("Enter student age: ")
rollno = raw_input("Enter student roll no: ")
branch = raw_input("Enter student branch: ")

values = {"Student_Name" : name, "Student_Age" : age, "Student_RollNo" : rollno, "Student_Branch" : branch}

data = json.dumps(values)
header = {"Content-Type":"application/json"}
req1 = urllib2.Request(insert_api, data, headers=header)
response1 = urllib2.urlopen(req1)
print response1.read()

search_rollno = raw_input("Enter Roll No. to view: ")

view_api = "https://api.mlab.com/api/1/databases/db_university/collections/students?q={'Student_RollNo':'"+search_rollno+"'}&fo=true&apiKey=cxzVW0OfZ_Nb1DtxpFHiXUdc0ChbyKzX"

req2 = urllib2.Request(view_api)
response2 = urllib2.urlopen(req2)
print response2.read()