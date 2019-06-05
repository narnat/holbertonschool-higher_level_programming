#!/usr/bin/python3
"""Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class, inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Constructor for Rectangle class"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String method"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
