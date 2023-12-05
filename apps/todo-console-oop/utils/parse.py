import json as _json
import time
from datetime import datetime

from models.task import Task as _Task

def parse_tasks(tasks):
    return [
        parse_task(task)
    for task in tasks]

def parse_task(task):
    return _Task(task[0], task[1], task[2], task[3], task[4], task[5])

def convert_datetime(date):
    if date == None:
        return date
    else: 
        return datetime.strptime(date, '%d/%m/%Y %H:%M:%S')

# The __dict__ in Python represents a dictionary or any mapping object that is used to store the attributes of the object.
def parse_to_json_array(data):
    return _json.dumps([ob.__dict__ for ob in data], indent = 4, ensure_ascii=False).encode('utf-8').decode('utf-8')

def parse_to_json(data):
    return _json.dumps(data.__dict__, indent = 4, ensure_ascii=False).encode('utf-8').decode('utf-8')
