#!/usr/bin/python3
"""Script that takes in a URL and an email"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    my_url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    req = urllib.request.Request(my_url, data)
    with urllib.request.urlopen(req) as response:
        message = response.read()

        print("{}".format(message.decode('utf-8')))
