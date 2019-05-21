#!/usr/bin/python3
"""Simple class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Constructor"""
        try:
            size += 0
        except:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
