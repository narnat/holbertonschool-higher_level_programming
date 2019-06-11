#!/usr/bin/python3
"""Base class"""
import json
import os


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base"""
        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def reset():
        """Resets the Base class"""
        Base._Base__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """To json the list of dictionaries"""
        if list_dictionaries in (None, []):
            return "[]"
        if type(list_dictionaries) != list and\
           all(type(d) != dict for d in list_dictionaries):
            return
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save json to file"""
        if list_objs is None:
            with open(cls.__name__+".json", "w") as file:
                file.write("[]")
        if list_objs and any(isinstance(j, Base) for j in list_objs):
            l = [i.to_dictionary() for i in list_objs]
            with open(cls.__name__+".json", "w") as file:
                file.write(Base.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """Converts from JSON"""
        if json_string is None:
            return []
        if json_string == [] or type(json_string) != str:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an object"""
        if not issubclass(cls, Base):
            return
        a = cls(32, 3)
        a.update(**dictionary)
        return a

    @classmethod
    def load_from_file(cls):
        """Create"""
        l = []
        name = cls.__name__+".json"
        if os.path.isfile(name):
            with open(name, "r") as file:
                s = cls.from_json_string(file.readline())
            for i in s:
                l.append(cls.create(**i))
            return l
        return []
