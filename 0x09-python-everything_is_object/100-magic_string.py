#!/usr/bin/python3
def magic_string():
    setattr(magic_string, "count", getattr(magic_string, "count", -1) + 1)
    return "Holberton" + ", Holberton" * magic_string.count
