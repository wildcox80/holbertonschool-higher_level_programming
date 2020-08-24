#!/usr/bin/python3
"""Script sends a request and displays the body of the response"""
import requests


if __name__ == "__main__":
    if __name__ == "__main__":
        res = requests.get('https://intranet.hbtn.io/status')

        print("Body response:")
        print("\t- type: {}".format(type(res.text)))
        print("\t- content: {}".format(res.text))
