#!/usr/bin/python3
""""Reads a file and outputs to stdout"""


def read_file(filename=""):
    """Reads from file"""

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
