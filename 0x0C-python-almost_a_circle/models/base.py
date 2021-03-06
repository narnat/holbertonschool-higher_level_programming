#!/usr/bin/python3
"""Base class"""
import json
import os
import csv
import turtle


class Base:

    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def reset():
        """Resets the Base class"""
        Base._Base__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """Takes a list of dicts and changes it to a json string
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save json to file"""
        if list_objs is None:
            with open(cls.__name__ + ".json", "w") as file:
                file.write("[]")
        else:
            l = [i.to_dictionary() for i in list_objs]
            with open(cls.__name__ + ".json", "w") as file:
                file.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """Converts from JSON"""
        if json_string is None:
            return []
        if json_string == [] or not isinstance(json_string, str):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an object"""
        if cls.__name__ == "Rectangle":
            a = cls(32, 3)
            a.update(**dictionary)
            return a
        if cls.__name__ == "Square":
            a = cls(32)
            a.update(**dictionary)
            return a

    @classmethod
    def load_from_file(cls):
        """Create"""
        l = []
        name = cls.__name__ + ".json"
        if os.path.isfile(name):
            with open(name, "r") as file:
                s = cls.from_json_string(file.read())
            for i in s:
                l.append(cls.create(**i))
            return l
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves to csv file"""
        if list_objs is None or not isinstance(list_objs, list) \
           or not all(isinstance(j, Base) for j in list_objs):
            with open(cls.__name__ + ".csv", "w") as file:
                file.write("[]")
        if list_objs and any(isinstance(j, Base) for j in list_objs):
            dict_data = [i.to_dictionary() for i in list_objs]
            if cls.__name__ == "Rectangle":
                csv_columns = ["id", "width", "height", "x", "y"]
            else:
                csv_columns = ["id", "size", "x", "y"]
            with open(cls.__name__ + ".csv", "w") as file:
                writer = csv.DictWriter(file, fieldnames=csv_columns)
                writer.writeheader()
                for data in dict_data:
                    writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        """Loads from csv file"""
        l = []
        name = cls.__name__ + ".csv"
        if os.path.isfile(name):
            with open(name, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    d = {key: int(value) for key, value in row.items()}
                    l.append(cls.create(**d))
            return l
        return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws sqaures and rectangles"""
        for i in list_rectangles + list_squares:
            tt = turtle.Turtle()
            tt.shape("turtle")
            turtle.bgcolor("black")
            tt.fillcolor("white")
            # turtle.color("white")
            tt.begin_fill()
            tt.pen(fillcolor="white", pencolor="red", pensize=2)
            for _ in range(2):
                tt.forward(i.width)
                tt.right(90)
                tt.forward(i.height)
                tt.right(90)
            tt.end_fill()
            turtle.done()
