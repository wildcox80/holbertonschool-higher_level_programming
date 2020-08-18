#!/bin/bash
#Script Body Size
curl -so /dev/null "$1" -w '%{size_download}\n'
