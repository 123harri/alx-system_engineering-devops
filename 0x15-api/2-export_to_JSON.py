#!/usr/bin/python3
"""
Script to fetch and display employee TODO list progress
from a REST API and export data in JSON format.
"""

import csv
import requests
import json
import sys
import re

REST_API = "https://jsonplaceholder.typicode.com"


def fetch_and_export_employee_todo_progress(employee_id):
    """
    Fetches employee TODO list progress and exports data in JSON format.
    """
    user_response = requests.get(f"{REST_API}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get('name')

    todos_response = requests.get(f"{REST_API}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    user_tasks = []
    for task in todos_data:
        user_tasks.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name,
            })

    json_filename = f"{employee_id}.json"
    with open(json_filename, mode='w') as jsonfile:
        json.dump({"USER_ID": user_tasks}, jsonfile, indent=4)

    print(f"Data exported to {json_filename}")


if __name__ == '__main__':
    if len(sys.argv) > 1 and re.fullmatch(r'\d+', sys.argv[1]):
        fetch_and_export_employee_todo_progress(int(sys.argv[1]))
    else:
        print("Usage: python3 todo_progress_json.py <employee_id>")
