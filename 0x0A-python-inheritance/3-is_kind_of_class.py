#!/usr/bin/python3
"""Checks instance of a Class"""


def is_kind_of_class(obj, a_class):
    """Uses isinstance to check if the obj belongs to a_class or subclasses"""
    return isinstance(obj, a_class)
