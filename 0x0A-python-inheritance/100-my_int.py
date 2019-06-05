#!/usr/bin/python3
"""MyInt Class"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, other):
        """Equal method"""
        return (str(self) != str(self))

    def __ne__(self, other):
        """Not equal method"""
        return (str(self) == str(self))
