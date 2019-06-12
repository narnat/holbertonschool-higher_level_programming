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

    def test_json_empty(self):
        """test json"""
        json_dictionary = Base.to_json_string([])
        self.assertEqual([], json.loads(json_dictionary))

    def test_json_none(self):
        """test json"""
        json_dictionary = Base.to_json_string(None)
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
