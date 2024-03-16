#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 0
if number < 0:
    number = number * -1
    sign = 1
else:
    sign = 0
ld = number % 10
if sign == 1:
    ld = ld * -1
    number = number * -1
if ld > 5:
    print(f"Last digit of {number:d} is {ld:d} and is greater than 5")
elif ld == 0:
    print(f"Last digit of {number:d} is {ld:d} and is 0")
else:
    print(f"Last digit of {number:d} is {ld:d} and is less than 6 and not 0")
