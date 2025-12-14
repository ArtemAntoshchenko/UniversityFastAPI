from fastapi import FastAPI
from utils import *
from typing import Optional
import os

script_dir=os.path.dirname(os.path.abspath(__file__))
parent_dir=os.path.dirname(script_dir)
path_to_json=os.path.join(parent_dir, 'students.json')

app=FastAPI()

@app.get('/students')
def get_all_students():
    return json_to_dict_list(path_to_json)