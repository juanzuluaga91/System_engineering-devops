#!/usr/bin/python3
"""Fake api for requests"""
import json
import requests
import sys


if __name__ == "__main__":
    try:
        employee_id = sys.argv[1]
    except:
        print("usage: ./{} employee_id".format(sys.argv[0]))
    namereq = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    name = json.loads(namereq.text)['name']

    r = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(employee_id))
    data = json.loads(r.text)

    started = len(data)
    finished = []

    for obj in data:
        if obj['completed'] is True:
            finished += ["\t {}".format(obj['title'])]

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(finished), started))
    for task in finished:
        print(task)
