#!/usr/bin/python3
"""
Funtion to gather data from an API
"""
import sys
import requests
import json


if __name__ == "__main__":
    # Check if number is ingeter
    def is_integer_num(n):
        if isinstance(n, int):
            return True
        if isinstance(n, float):
            return n.is_integer()
        return False

    # URL's to get all information
    url_user = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    url_tasks = ('https://jsonplaceholder.typicode.com/users/'
                 + sys.argv[1] + '/todos')

    # Get data response whit requests
    r_user = requests.get(url_user)
    r_tasks = requests.get(url_tasks)

    # Set data response to json
    obj_user = json.loads(r_user.text)
    obj_task = json.loads(r_tasks.text)

    task_done = 0
    TASK_TITLE = ""
    for task in obj_task:
        TASK_TITLE += "\t" + task["title"] + "\n"
        if task["completed"] is True:
            task_done += 1

    NUMBER_OF_DONE_TASKS = 'a'
    EMPLOYEE_NAME = obj_user["name"]
    NUMBER_OF_DONE_TASKS = task_done
    TOTAL_NUMBER_OF_TASKS = len(obj_task)
    print("Employee %s is done with tasks(%d/%d):\n %s" %
          (EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS,
           TOTAL_NUMBER_OF_TASKS, TASK_TITLE), end="")
