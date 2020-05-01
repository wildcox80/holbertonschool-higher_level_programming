#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum_all = len(argv) - 1
    res = 0
    for i in range(1, sum_all + 1):
        res += int(argv[i])
    print("{:d}".format(res))
