#!/usr/bin/python3
"""Saves JSON into a file"""
import json


def save_to_json_file(my_obj, filename):
    """Save JSON to a file"""

    with open(filename, 'w') as f:
        a = json.dumps(my_obj)
        f.write(a)
