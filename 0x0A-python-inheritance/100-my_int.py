#!/usr/bin/python3
"""MyInt Class"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, other):
        """Equal method"""
        return super().__ne__(self)

    def __ne__(self, other):
        """Not equal method"""
        return super().__eq__(self)
