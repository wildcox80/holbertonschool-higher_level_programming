#!/usr/bin/python3
"""Script that takes in a URL and an email address, sends a POST request"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    arg_length = len(sys.argv)
    if arg_length == 2:
        q = sys.argv[1]
    else:
        q = ""

    req = requests.post(url, data={'q': q})

    try:
        req = req.json()
        if not req:
            print('No result')
        else:
            print('[{}] {}'.format(req['id'], req['name']))

    except ValueError:
        print('Not a valid JSON')
