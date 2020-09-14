#!/usr/bin/python3
"""
Funtion to gather data from an API
"""
import json
import sys
import requests


if __name__ == "__main__":
    # Check if number is ingeter
    def is_integer(n):
        try:
            float(n)
        except ValueError:
            return False
        else:
            return float(n).is_integer()

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
        obj_user = json.loads(r_user.text)
        obj_task = json.loads(r_tasks.text)

        task_done = 0
        TASK_TITLE = ""
        for task in obj_task:
            if task["completed"] is True:
                TASK_TITLE += "\t" + task["title"] + "\n"
                task_done += 1

        EMPLOYEE_NAME = obj_user["name"]
        NUMBER_OF_DONE_TASKS = task_done
        TOTAL_NUMBER_OF_TASKS = len(obj_task)
        print("Employee %s is done with tasks(%d/%d):\n %s" %
              (EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS,
               TOTAL_NUMBER_OF_TASKS, TASK_TITLE), end="")
