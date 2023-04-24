#!/usr/bin/python3
"""
Using this REST API (https://jsonplaceholder.typicode.com/), for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todos_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    num_of_total_tasks = len(todos_data)
    num_of_done_tasks = sum(1 for task in todos_data if task['completed'])

    print("Employee {} is done with tasks({}/{}):".format(
        user_data['name'], num_of_done_tasks, num_of_total_tasks))
    for task in todos_data:
        if task['completed']:
            print("\t {}".format(task['title']))

