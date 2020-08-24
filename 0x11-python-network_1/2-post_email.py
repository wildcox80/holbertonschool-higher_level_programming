#!/usr/bin/python3
"""Script that takes in a URL and an email"""
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    values = parse.urlencode(values).encode('utf-8')
    req = request.Request(url, values)

    with request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
        print(the_page)
