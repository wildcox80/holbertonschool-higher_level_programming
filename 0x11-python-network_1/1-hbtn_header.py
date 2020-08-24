#!/usr/bin/python3
"""Script that displays the value of the X-Request-Id"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        headers = response.info()
        print(headers.get('X-Request-Id'))
