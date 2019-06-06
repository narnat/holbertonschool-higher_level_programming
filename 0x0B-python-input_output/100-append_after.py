#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """Search and update"""
    with open(filename, 'r') as f:
        s = f.readlines()

    with open(filename, 'w') as f:
        for i in s:
            if search_string in i:
                i += new_string
            f.write(i)
