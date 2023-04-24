#!/usr/bin/env python3
import csv
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: {} <employee_id>".format(sys.argv[0]))
    sys.exit(1)

# Define the API endpoint URL and the target employee's ID
url = "https://jsonplaceholder.typicode.com/todos"
employee_id = int(sys.argv[1])

# Send a GET request to the API endpoint
response = requests.get(url)

# Check if the response is successful (status code 200)
if response.status_code != 200:
    print("Failed to retrieve tasks: status code {}".format(response.status_code))
    sys.exit(1)

# Parse the response data as JSON
tasks = response.json()

# Filter the tasks that are assigned to the target employee
employee_tasks = [task for task in tasks if task["userId"] == employee_id]

# Define the output CSV filename
filename = "{}.csv".format(employee_id)

# Write the employee tasks to the CSV file
with open(filename, mode='w', newline='') as csv_file:
    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for task in employee_tasks:
        writer.writerow({
            'USER_ID': task['userId'],
            'USERNAME': '',  # We don't have access to usernames in the API response
            'TASK_COMPLETED_STATUS': str(task['completed']),
            'TASK_TITLE': task['title']
        })

print("Task data exported to file: {}".format(filename))

