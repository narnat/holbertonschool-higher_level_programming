#!/usr/bin/python3
"""Test cases for Rectangle class, task 4"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass_area(unittest.TestCase):

    """Test cases for ractangle, task 3"""

    def setUp(self):
        """Teardown"""
        Base.reset()

    def test_area(self):
        """Simple area test"""
        r = Rectangle(32, 2)
        self.assertEqual(r.area(), 64)
