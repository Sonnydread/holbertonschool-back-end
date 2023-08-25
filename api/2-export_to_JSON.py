#!/usr/bin/python3
"""extend the script to export data in the JSON format"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    source = f"https://jsonplaceholder.typicode.com/user/{argv[1]}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    user_response = requests.get(source)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    listall = []

    for todo in todos_data:
        todo_direct = {
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': user_data.get('username')
        }
        listall.append(todo_direc)

    zm = {f"{argv[1]}": listall}
    with open(f"{argv[1]}.json", 'w') as file:
        json.dump(zm, file, indent=4)

    print(f"Data saved to {argv[1]}.json")
