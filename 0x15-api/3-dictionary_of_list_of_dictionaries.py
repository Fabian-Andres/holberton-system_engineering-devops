#!/usr/bin/python3
"""
Funtion to dictionary of list of dictionaries
"""
import json
import requests
import sys


if __name__ == "__main__":

    # URL's to get all information
    url = 'https://jsonplaceholder.typicode.com'
    url_users = (url + '/users/')

    # Get data response whit requests
    r_users = requests.get(url_users)
    # Set data response to json
    obj_users = r_users.json()

    dic_users = {}
    for user in obj_users:
        # Get tasks response whit requests
        url_tasks = (url + '/users/' + str(user['id']) + '/todos')
        # Get data response whit requests
        r_tasks = requests.get(url_tasks)
        # Set data response to json
        obj_task = r_tasks.json()

        dic_tasks = []
        # Adding users into dictionary
        dic_users.update({user["id"]: dic_tasks})

        # Set list of dictionaries
        for task in obj_task:
            dic_tasks.append({
                "task": task["title"],
                "completed": task["completed"],
                "username": user["username"]
            })

    file = open("todo_all_employees.json", 'w')
    file.write(json.dumps(dic_users))
    file.close()
