#!/usr/bin/python3
"""Test cases for Rectangle class, task 7"""
import unittest
from models.rectangle import Rectangle
import io
from contextlib import redirect_stdout
from models.base import Base


class TestRectangleClass_Display(unittest.TestCase):

    """Test cases for ractangle, task 7"""

    def tearDown(self):
        """Teardown"""
        Base.reset()

    def test_display(self):
        """Test display with valid arguments"""
        f = io.StringIO()
        s = ('#' * 4 + '\n') * 3
        r1 = Rectangle(4, 3)
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), s)

        f = io.StringIO()
        s = ('\n' * 2) + (" " * 2 + '#' * 2 + '\n') * 3
        r1 = Rectangle(2, 3, 2, 2)
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), s)
