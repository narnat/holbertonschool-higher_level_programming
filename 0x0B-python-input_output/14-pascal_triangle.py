#!/usr/bin/python3
"""Pascal triangle"""
from math import factorial as fc


def pascal_triangle(n):
    """Pascal Triangle"""
    a = []
    if n <= 0:
        return a
    for i in range(n):
        b = []
        for j in range(i + 1):
            b.append(int(fc(i)/(fc(j) * fc(i - j))))
        a.append(b)
    return a
