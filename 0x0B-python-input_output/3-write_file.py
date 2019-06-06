#!/usr/bin/python3
"""Writes to a file"""


def write_file(filename="", text=""):
    """Writes to a file"""

    with open(filename, 'w', encoding='utf-8') as f:
        c = f.write(text)
    return c
