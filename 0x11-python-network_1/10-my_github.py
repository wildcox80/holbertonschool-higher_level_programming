#!/usr/bin/python3
"""Script that takes your Github credentials"""
import requests
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    r = requests.get('https://api.github.com/user',
                     params={"login": username},
                     auth=(username, password)).json()
    if "id" in r:
        print(r["id"])
    else:
        print(None)
