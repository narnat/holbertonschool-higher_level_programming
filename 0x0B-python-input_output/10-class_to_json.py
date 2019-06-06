#!/usr/bin/python3
"""Simple JSON parser"""


def class_to_json(obj):
    """Json converter"""

    if hasattr(obj, '__dict__'):
        return obj.__dict__
