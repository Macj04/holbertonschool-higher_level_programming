#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if last_digit > 5:
    status = "is greater than 5"
elif last_digit < 6 and last_digit != 0:
    status = "is less than 6 and not 0"
else:
    status = "is 0"

print("Last digit of {0} is {1} and {2}".format(number, last_digit, status))
