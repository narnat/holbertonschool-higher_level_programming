#!/usr/bin/python3
"""Test cases for Square class"""
import unittest
import inspect
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

    def test_create(self):
        """Test create"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        r1 = Square(3, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Square] (3) 1/0 - 3")
        self.assertEqual(str(r2), "[Square] (3) 1/0 - 3")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_wrong(self):
        """Wrong number of args"""
        with self.assertRaises(TypeError):
            Rectangle.create("Hi")

        with self.assertRaises(TypeError):
            Square.create("Go")
        self.assertEqual(Base.create(), None)

    def test_classmethod(self):
        """Checks class method"""
        self.assertTrue(inspect.ismethod(Base.create))
