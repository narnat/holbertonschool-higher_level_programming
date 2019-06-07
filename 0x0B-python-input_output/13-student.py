#!/usr/bin/python3
"""Student Class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """To JSON"""
        if attrs is None:
            return self.__dict__
        d = {}
        if type(attrs) == list and all(type(i) == str for i in attrs):
            for el in attrs:
                if el in self.__dict__:
                    d[el] = self.__dict__[el]
            return d

    def reload_from_json(self, json):
        """Reloads JSON file"""
        for keys in json:
            self.__dict__[keys] = json[keys]
