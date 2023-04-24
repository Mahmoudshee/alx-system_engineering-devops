#!/usr/bin/python3
"""
Script that exports data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + user_id
    response = requests.get(url)
    name = response.json().get('username')

    url = "https://jsonplaceholder.typicode.com/todos"
    params = {'userId': user_id}
    response = requests.get(url, params=params)
    tasks = response.json()

    user_tasks = {}
    for task in tasks:
        task_dict = {}
        task_dict['task'] = task.get('title')
        task_dict['completed'] = task.get('completed')
        task_dict['username'] = name

        if user_id not in user_tasks:
            user_tasks[user_id] = []

        user_tasks[user_id].append(task_dict)

    with open(user_id + '.json', 'w') as json_file:
        json.dump(user_tasks, json_file)

