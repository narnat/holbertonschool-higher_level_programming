#!/usr/bin/python3
"""Adds attribute to the object"""


def add_attribute(cls, name, value):
    """Adds attribute to cls"""
    if "__dict__" not in dir(cls) and "__slots__" not in dir(cls):
        raise TypeError("can't add new attribute")
    if hasattr(cls, "__slots__"):
        if name not in cls.__slots__:
            raise TypeError("can't add new attribute")
    cls.name = value
