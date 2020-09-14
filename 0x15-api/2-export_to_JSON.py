#!/usr/bin/python3
"""
Funtion to export to JSON
"""
import json
import requests
import sys


if __name__ == "__main__":
    # Check if number is ingeter
    def is_integer(n):
        try:
            float(n)
        except ValueError:
            return False
        else:
            return float(n).is_integer()

    # Check len
    if len(sys.argv) < 2:
        sys.exit()

    n_id = sys.argv[1]

    if is_integer(n_id):
        # URL's to get all information
        url = 'https://jsonplaceholder.typicode.com'
        url_user = (url + '/users/' + n_id)
        url_tasks = (url + '/users/' + n_id + '/todos')

        # Get data response whit requests
        r_user = requests.get(url_user)
        r_tasks = requests.get(url_tasks)

        # Set data response to json
        obj_user = r_user.json()
        obj_task = r_tasks.json()

        dic_tasks = []
        file = open(str(n_id)+".json", 'w')
        for task in obj_task:
            dic_tasks.append({
                "task": task["title"],
                "completed": task["completed"],
                "username": obj_user["username"]
            })
        file.write(json.dumps({task["userId"]: dic_tasks}))
        file.close()
