#!/usr/bin/python
from __future__ import print_function
from datetime import time
from tasklib import Task, local_zone

DEFAULT_TIME = time(21,0,0)  # Your wanted default time
DEFAULT_WORK_TIME = time(17,0,0) #Default Work Time
def is_local_midnight(timestamp):
    return timestamp.astimezone(local_zone).time() == time(0,0,0)

def set_default_time(timestamp, defTime):
    return timestamp.astimezone(local_zone).replace(
        hour=defTime.hour,
        minute=defTime.minute,
        second=defTime.second,
        )

def hook_default_time(task):
    if task['due'] and is_local_midnight(task['due']):
	if '@work' in task['tags']:
		task['due'] = set_default_time(task['due'], DEFAULT_WORK_TIME)
		print("Default due time has been set to work default.")
	else: 
        	task['due'] = set_default_time(task['due'], DEFAULT_TIME)
        	print("Default due time has been set.")
