#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number1 = 0
if number < 0:
    number1 = number * -1
    remainder = number1 % 10
else:
    remainder = number % 10
if remainder > 5:
    print(f"Last digit of {number} is {remainder} and is greater than 5")
elif remainder == 0:
    print(f"Last digit of {number} is {remainder} and is 0")
elif remainder > 0:
    print(f"Last digit of {number} is {remainder} and is less than 6 and not 0")
