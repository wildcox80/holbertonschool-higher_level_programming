#!/usr/bin/python3
""" Script fetch https://intranet.hbtn.io/status """

import urllib.request


if __name__ == "__main__":
    req = "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print(req.format(type(html), html, html.decode("utf-8"), end=""))
