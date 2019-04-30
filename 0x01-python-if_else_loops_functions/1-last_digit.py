#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ten = 10
if number < 0:
    ten = -10
n = number % ten
print("Last digit of", end=' ')
if n > 5:
    print("{:d} is {:d} and is greater than 5".format(number, n))
elif n == 0:
    print("{:d} is {:d} and is 0".format(number, n))
else:
    print("{:d} is {:d} and is less than 6 and not 0".format(number, n))
