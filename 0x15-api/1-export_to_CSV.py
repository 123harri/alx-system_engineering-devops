#!/usr/bin/python3
"""
Script to fetch and display employee TODO list progress
from a REST API and export data in CSV format.
"""

import re
import requests
import csv
import sys

REST_API = "https://jsonplaceholder.typicode.com"


def fetch_and_export_employee_todo_progress(employee_id):
    """
    Fetches employee TODO list progress and exports data in CSV format.
    """
    user = requests.get(f"{REST_API}/users/{employee_id}").json()
    name = user.get('name')
    tasks = requests.get(f"{REST_API}/todos?userId={employee_id}").json()

    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USER_ID", "USERNAME", "COMPLETED", "TITLE"])
        w = writer.writerow
        for task in tasks:
            w([employee_id, name, task['completed'], task['title']])

    print(f"Data exported to {filename}")


if __name__ == '__main__':
    if len(sys.argv) > 1 and re.fullmatch(r'\d+', sys.argv[1]):
        fetch_and_export_employee_todo_progress(int(sys.argv[1]))
    else:
        print("Usage: python3 todo_progress_csv.py <employee_id>")
