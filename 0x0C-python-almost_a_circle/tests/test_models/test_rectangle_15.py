#!/usr/bin/python3
"""Test cases for Square class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import io
import json
from contextlib import redirect_stdout


class TestBaseClass_to_json(unittest.TestCase):

    """Test Base"""

    def setUp(self):
        """Resets __nb_objects"""
        Base.reset()

    def test_json(self):
        """test json"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual([dictionary], json.loads(json_dictionary))

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Rectangle.to_json_string([dictionary])
        self.assertEqual([dictionary], json.loads(json_dictionary))

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Square.to_json_string([dictionary])
        self.assertEqual([dictionary], json.loads(json_dictionary))

    def test_json_empty(self):
        """test json"""
        json_dictionary = Base.to_json_string([])
        self.assertEqual([], json.loads(json_dictionary))

        json_dictionary = Rectangle.to_json_string([])
        self.assertEqual([], json.loads(json_dictionary))

        json_dictionary = Square.to_json_string([])
        self.assertEqual([], json.loads(json_dictionary))

    def test_json_none(self):
        """test json"""
        json_dictionary = Base.to_json_string(None)
        self.assertEqual([], json.loads(json_dictionary))

        json_dictionary = Rectangle.to_json_string(None)
        self.assertEqual([], json.loads(json_dictionary))

        json_dictionary = Square.to_json_string(None)
        self.assertEqual([], json.loads(json_dictionary))

    def test_json_multiple(self):
        """test json"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(14, 2, 5, 8)
        dictionary = r1.to_dictionary()
        dictionary1 = r2.to_dictionary()
        ss = [dictionary, dictionary1]
        json_dictionary = Base.to_json_string(ss)
        self.assertEqual(ss, json.loads(json_dictionary))

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(14, 2, 5, 8)
        dictionary = r1.to_dictionary()
        dictionary1 = r2.to_dictionary()
        ss = [dictionary, dictionary1]
        json_dictionary = Rectangle.to_json_string(ss)
        self.assertEqual(ss, json.loads(json_dictionary))

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(14, 2, 5, 8)
        dictionary = r1.to_dictionary()
        dictionary1 = r2.to_dictionary()
        ss = [dictionary, dictionary1]
        json_dictionary = Square.to_json_string(ss)
        self.assertEqual(ss, json.loads(json_dictionary))

    def test_exceptions(self):
        """test exceptions"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

        with self.assertRaises(TypeError):
            Base.to_json_string(32, 323, 323, 32)

        with self.assertRaises(TypeError):
            Rectangle.to_json_string()

        with self.assertRaises(TypeError):
            Rectangle.to_json_string(32, 323, 323, 32)

        with self.assertRaises(TypeError):
            Square.to_json_string()

        with self.assertRaises(TypeError):
            Square.to_json_string(32, 323, 323, 32)

    def test_notlist(self):
        """Checks not list type"""
        with self.assertRaises(TypeError):
            Base.to_json_string(32)

    def test_notlist_ofobjs(self):
        """Checks list of objs"""
        with self.assertRaises(AttributeError):
            Base.to_json_string([32, 3])
