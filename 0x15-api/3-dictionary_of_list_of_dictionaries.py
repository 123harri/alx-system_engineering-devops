#!/usr/bin/python3
"""
Script to fetch and display employee TODO list progress from a
REST API and export data for all employees in JSON format.
"""

import json
import requests
import sys

if __name__ == '__main__':
    url_to_users = 'https://jsonplaceholder.typicode.com/users'
    users_response = requests.get(url_to_users)
    users_data = users_response.json()

    all_tasks = {}
    for user in users_data:
        user_id = str(user['id'])
        username = user['username']
        url_to_tasks = f'https://jsonplaceholder.typicode.com/users/' \
                       f'{user_id}/todos'
        tasks_response = requests.get(url_to_tasks)
        tasks_data = tasks_response.json()

        user_tasks = []
        for task in tasks_data:
            user_tasks.append({
                "task": task['title'],
                "completed": task['completed'],
                "username": username
            })

        all_tasks[user_id] = user_tasks

    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_tasks, f, indent=4)
