#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = abs(number) % 10
if number < 0:
    temp = -temp
print(f'Last digit of {number} is {temp}', end='')
if temp > 5:
    print(' and is greater than 5')
if temp == 0:
    print(' and is 0')
if temp < 6 and temp != 0:
    print(' and is less than 6 and not 0')
