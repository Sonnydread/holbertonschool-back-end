#!/usr/bin/python3
"""extend the script to export data in the JSON format"""

import requests
from requests import get
from sys import argv
from json import dump


if __name__ == '__main__':
    source = "https://jsonplaceholder.typicode.com/user/{}/todos".format(
        argv[1])
    names = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    todores = get(source).json()
    nameres = get(names).json()

    listall = []
    for todo in todores:
        todo_direct = {}
        todo_direct.update({"task": todo.get("title"), "completed": todo.get(
            "completed"), "username": name_result.get("username")})
        listall.append(todo_direct)

    with open("{}.json".format(argv[1]), 'w') as f:
        dump({argv[1]: listall}, f)
