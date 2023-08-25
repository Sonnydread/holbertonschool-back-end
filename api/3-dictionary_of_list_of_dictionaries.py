#!/usr/bin/python3
"""extend the script to export data in the JSON format"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    source = "https://jsonplaceholder.typicode.com/users/"
    allusers = requests.get(source)
    todo_direct = {}

    for z in allusers.json():
        xyz = f"https://jsonplaceholder.typicode.com/users/{z.get('id')}/todos"
        todo = requests.get(xyz)
        cont = []

        for x in todo.json():
            kes = {'username': f"{z.get('username')}",
                   'task': f"{x.get('title')}",
                   'completed': x.get('completed')}
            cont.append(kes)
        todo_direct[f"{z.get('id')}"] = cont

    with open("todo_all_employees.json", 'w') as file:
        json.dump(todo_direct, file)
