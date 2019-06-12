#!/usr/bin/python3
"""Test cases for r1.update class, task 9"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
from contextlib import redirect_stdout


class TestRectangleClass_Updates(unittest.TestCase):

    """Test cases for ractangle, task 9"""

    def setUp(self):
        """Teardown"""
        Base.reset()

    def test_args_order(self):
        """Checks correct order of arguments"""
        f = io.StringIO()
        s = "[Rectangle] (1) 10/10 - 10/89"
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=89)
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        r1.update(width=1, x=2)
        f = io.StringIO()
        s = "[Rectangle] (1) 2/10 - 1/89"
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        r1.update(y=1, width=2, x=3, id=89)
        f = io.StringIO()
        s = "[Rectangle] (89) 3/1 - 2/89"
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        r1.update(x=1, height=2, y=3, width=4)
        f = io.StringIO()
        s = "[Rectangle] (89) 1/3 - 4/2"
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)
