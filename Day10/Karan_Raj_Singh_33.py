# -*- coding: utf-8 -*-
"""
Created on Wed May 23 11:49:43 2018

@author: Karan
"""

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

mydb = client.db_University

def add_student(Student_Name, Student_Age, Student_RollNo, Student_Branch):
    unique_student = mydb.students.find_one({"Student_RollNo" : Student_RollNo})
    if unique_student:
        return "Student already exist"
    else:
        mydb.students.insert(
                {
                "Student_Name" : Student_Name,
                "Student_Age" : Student_Age,
                "Student_RollNo" : Student_RollNo,
                "Student_Branch" : Student_Branch
                })
        return "Student Added Successfully"
    
def view_student(Student_RollNo):
    student = mydb.students.find_one({"Student_RollNo" : Student_RollNo})
    if student:
        name = student["Student_Name"]
        age = student["Student_Age"]
        rollno = student["Student_RollNo"]
        branch = student["Student_Branch"]
        return {"Student_Name" : name, "Student_Age" : age, "Student_RollNo" : rollno, "Student_Branch" : branch}
    
#main script
name = raw_input("Enter student name: ")
age = raw_input("Enter student age: ")
rollno = raw_input("Enter student roll no: ")
branch = raw_input("Enter student branch: ")

print add_student(name, age, rollno, branch)

ref_rollno = raw_input("Enter student roll no to show database: ")

print view_student(ref_rollno)