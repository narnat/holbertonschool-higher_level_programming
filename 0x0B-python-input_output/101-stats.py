#!/usr/bin/python3
"""Log Parser"""
import signal
from sys import stdin


def printer(size, d):
    """Printer function"""
    a = sorted(d.keys())
    print("File size:", size)
    for i in a:
        if d[i] != 0:
            print("{}: {}".format(i, d[i]))

size = 0
d = {"200": 0, "301": 0, "400": 0, "401": 0,
     "403": 0, "404": 0, "405": 0, "500": 0}


def handler(signum, frame):
    printer(size, d)

counter = 1
signal.signal(signal.SIGINT, handler)
# with open(0) as f:
for line in stdin:
    arr = line.split()
    size += int(arr[-1])
    d[arr[-2]] += 1
    if counter % 10 == 0:
        printer(size, d)
    counter += 1
