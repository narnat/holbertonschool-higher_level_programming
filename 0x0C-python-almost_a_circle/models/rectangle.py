#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):

    """Rectangle class which inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Contructor for Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of the rectangle"""
        return self.height * self.width

    def display(self):
        """"Draws the rectangle"""
        print("\n" * self.y, end="")
        print((" " * self.x + "#" * self.width + '\n') * self.height, end="")

    def __str__(self):
        """String method for Rectangle class"""
        s = "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)
        return s

    def update(self, *args, **kwargs):
        """Updates Rectangle class"""
        if not args and not kwargs:
            return
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, e in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], e)
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """Converts to dictionary"""
        d = {}
        for k, v in self.__dict__.items():
            if k.startswith("_"):
                d[k.split("__")[-1]] = v
            else:
                d[k] = v
        return d
