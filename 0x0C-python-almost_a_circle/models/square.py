#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):

    """Sqaure class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constractor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String method for Rectangle class"""
        s = "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
        return s

    def area(self):
        """Returns area of the square"""
        return self.width ** 2

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value

    def update(self, *args, **kwargs):
        """Updates Square class"""
        if not args and not kwargs:
            return
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, e in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], e)
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """Converts to dictionary"""
        d = super().to_dictionary()
        d["size"] = d["width"]
        del d["width"], d["height"]
        return d
