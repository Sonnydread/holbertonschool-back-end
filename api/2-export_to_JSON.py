#!/usr/bin/python3
"""extend the script to export data in the JSON format"""

import json
from json import dump
import requests
from requests import get
from sys import argv


if __name__ == '__main__':
    source = f"https://jsonplaceholder.typicode.com/user/{argv[1]}"
    names = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    uss = requests.get(source)
    alltod = requests.get(names)
    listall = []

    for z in todo.json():
        todo_direct = {'task': f"{z.get('title')}",
                       'completed': z.get('completed'),
                       'username': f"{user.json().get('username')}"}
        listall.append(todo_direc)

    zm = {f"{argv[1]}": listall}
    with open(f"{argv[1]}.json", 'w') as file:
        json.dump(zm, file)
