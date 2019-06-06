#!/usr/bin/python3
"""Opens JSON file"""
import json


def load_from_json_file(filename):
    """Loads JSON file"""
    with open(filename, 'r') as f:
        a = json.load(f)
    return a
