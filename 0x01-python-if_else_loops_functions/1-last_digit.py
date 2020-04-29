#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    operator = -1
else:
    operator = 1
digit = operator * (operator * number % 10)
print("Last digit of {:d} is {:d} and is".format(number, digit), end=" ")
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
