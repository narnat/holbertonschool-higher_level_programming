#!/usr/bin/python3
"""BaseGeometry Class"""


class BaseGeometry:
    """BaseGeometry Class"""

    def area(self):
        """Area, not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if value is integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
