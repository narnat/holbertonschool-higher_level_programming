#!/usr/bin/python3
"""Returns number of lines in a text file"""


def number_of_lines(filename=""):
    """Return number of lines"""

    c = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for _ in f:
            c += 1
    return c
