#!/usr/bin/python3
"""Adds attribute to the object"""


def add_attribute(cls, name, value):
    """Adds attribute to cls"""
    if cls.__class__.__name__.islower():
        raise TypeError("can't add new attribute")
    cls.name = value
