#!/usr/bin/python3
"""Unittest for max_integer([..])
   Contains:
   TestMaxInteger
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test for max integer"""

    def test_basic_check(self):
        """Basic Check"""
        self.assertEqual(max_integer([3, 23, 54]), 54)

    def test_the_same_check(self):
        """Test the same numbers"""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_begin_check(self):
        """Test the beginning numbers"""
        self.assertEqual(max_integer([103, 3, 3]), 103)

    def test_middle_check(self):
        """Test the middle numbers"""
        self.assertEqual(max_integer([3, 43, 3]), 43)

    def test_one_neg_check(self):
        """Test one negative numbers"""
        self.assertEqual(max_integer([3, 43, -33]), 43)

    def test_neg_check(self):
        """Test only negative numbers"""
        self.assertEqual(max_integer([-3, -43, -33]), -3)

    def test_one_check(self):
        """Test only one number"""
        self.assertEqual(max_integer([-3]), -3)

    def test_empty_check(self):
        """Test empty list"""
        self.assertFalse(max_integer([]))

    def test_non_integer_check(self):
        """Test list with non integer elements"""
        with self.assertRaises(TypeError):
            max_integer([21, "21", 213])

if __name__ == '__main__':
    unittest.main()
