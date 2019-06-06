#!/usr/bin/python3
"""Reads at most nb_lines from a file"""


def read_lines(filename="", nb_lines=0):
    """Reads at most nb_lines"""

    c = 0
    if nb_lines <= 0:
        c = -1
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
            if c != -1:
                c += 1
                if c == nb_lines:
                    break
