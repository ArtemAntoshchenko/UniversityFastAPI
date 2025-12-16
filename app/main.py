from fastapi import FastAPI
from utils import *
from typing import Optional
import os

script_dir=os.path.dirname(os.path.abspath(__file__))
parent_dir=os.path.dirname(script_dir)
path_to_json=os.path.join(parent_dir, 'students.json')

app=FastAPI()

@app.get('/')
def home_page():
    return {'message':'Hello Python 47'}

# @app.get('/students')
# def get_all_students(course:Optional[int]=None):
#     students=json_to_dict_list(path_to_json)
#     if course is None:
#         return students
#     else:
#         return_list=[]
#         for student in students:
#             if student['course']==course:
#                 return_list.append(student)
#         return return_list

# @app.get('/students/{course}')
# def get_students_in_course(course:int, major:Optional[str]=None, enrollment_year:Optional[int]=None):
#     students=json_to_dict_list(path_to_json)
#     filtered_students=[]
#     for student in students:
#         if student['course']==course:
#             filtered_students.append(student)
#     if major:
#         filtered_students=[student for student in filtered_students if student['major'].lower()==major.lower()]
#     if enrollment_year:
#         filtered_students=[student for student in filtered_students if student['enrollment_year']==enrollment_year]
#     return filtered_students

@app.get('/students/{student_id}')
def get_student_by_id1(student_id:int):
    students=json_to_dict_list(path_to_json)
    for student in students:
        if student['student_id']==student_id:
            return student

@app.get('/students')
def get_student_by_id2(student_id:Optional[int]=None):
    students=json_to_dict_list(path_to_json)
    if student_id is None:
        return students
    else:
        for student in students:
             if student['student_id']==student_id:
                 return student