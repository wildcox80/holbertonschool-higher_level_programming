#!/usr/bin/python3
"""Script displays the value of the variable X-Request-Id"""
import requests
import sys


if __name__ == "__main__":
    result = requests.get(sys.argv[1])
    request_id = result.headers.get("X-Request-Id")
    print(request_id)
