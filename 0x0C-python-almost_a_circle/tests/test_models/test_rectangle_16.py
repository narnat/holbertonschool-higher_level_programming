#!/usr/bin/python3
"""Test cases for Square class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import io
import json
import os
from contextlib import redirect_stdout


class TestBaseClass_to_json(unittest.TestCase):

    """Test Base"""

    def setUp(self):
        """Resets __nb_objects"""
        Base.reset()

    def test_file(self):
        """test file"""
        file = "Rectangle.json"
        d = [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},
             {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open(file, "r") as file:
            self.assertEqual(json.loads(file.read()), d)

    def test_file_exists(self):
        """test file"""
        file = "Rectangle.json"
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.isfile(file))

    def test_file_overwrite(self):
        """test file"""
        file = "Rectangle.json"
        with open(file, "w") as f:
            f.write("Hi")
        d = [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},
             {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open(file, "r") as f:
            self.assertEqual(json.loads(f.read()), d)

    def test_file_s(self):
        """test file"""
        file = "Square.json"
        d = [{"y": 8, "x": 2, "id": 1, "size": 10},
             {"y": 0, "x": 0, "id": 2, "size": 2}]
        r1 = Square(10, 2, 8)
        r2 = Square(2)
        Square.save_to_file([r1, r2])

        with open(file, "r") as f:
            self.assertEqual(json.loads(f.read()), d)

    def test_file_exists_s(self):
        """test file"""
        file = "Square.json"
        r1 = Square(10, 2, 8)
        r2 = Square(2)
        Square.save_to_file([r1, r2])
        self.assertTrue(os.path.isfile(file))

    def test_file_overwrite_s(self):
        """test file"""
        file = "Square.json"
        with open(file, "w") as f:
            f.write("Hi")
        d = [{"y": 8, "x": 2, "id": 1, "size": 10},
             {"y": 0, "x": 0, "id": 2, "size": 2}]
        r1 = Square(10, 2, 8)
        r2 = Square(2)
        Square.save_to_file([r1, r2])

        with open(file, "r") as f:
            self.assertEqual(json.loads(f.read()), d)