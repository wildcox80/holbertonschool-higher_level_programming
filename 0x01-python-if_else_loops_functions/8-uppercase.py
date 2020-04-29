#!/usr/bin/python3
def islower(c):
    return ord(c) >= ord('a') and ord(c) <= ord('z')


def uppercase(str):
    toUpper = ord('a') - ord('A')
    for c in str:
        print("{}".format(chr(ord(c) - toUpper) if islower(c) else c), end="")
    print()
