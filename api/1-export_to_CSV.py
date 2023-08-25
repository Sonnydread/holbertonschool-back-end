#!/usr/bin/python3
"""extend the script to export data in the CSV format"""

import requests
from requests import get
from sys import argv
from csv import DictWriter, QUOTE_ALL


if __name__ == '__main__':
    source = 'https://jsonplaceholder.typicode.com'
    todoall = source + "/user/{}/todos".format(argv[1])
    names = source + "/users/{}".format(argv[1])
    todores = get(todoall).json()
    nameres = get(names).json()

    listall = []
    for todo in todores:
        todo_direct = {}
        todo_direct.update({"user_ID": argv[1], "username": nameres.get(
            "username"), "completed": todo.get("completed"),
                          "task": todo.get("title")})
        listall.append(todo_direct)
    with open("{}.csv".format(argv[1]), 'w', newline='') as f:
        header = ["user_ID", "username", "completed", "task"]
        writer = DictWriter(f, fieldnames=header, quoting=QUOTE_ALL)
        writer.writerows(listall)
