#!/usr/bin/python3
"""Test cases for BASE class"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):

    """Test cases for base class"""

    def test_id_valid(self):
        """Check only one instance"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_valid_multiple(self):
        """Check multiple instances"""
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 3)
        b3 = Base()
        self.assertEqual(b3.id, 4)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 5)

    def test_id_valid_same_id(self):
        """Check if instances have the same id"""
        b6 = Base(77)
        self.assertEqual(b6.id, 77)
        b7 = Base(77)
        self.assertEqual(b7.id, 77)

    def test_id_valid_param_str(self):
        """Check str as id"""
        b8 = Base("Holberton")
        self.assertEqual(b8.id, "Holberton")

    def test_id_valid_param_list(self):
        """Check list as id"""
        b9 = Base([98, 977])
        self.assertEqual(b9.id, [98, 977])

    def test_id_valid_param_tuple(self):
        """Check tuple as id"""
        b10 = Base((98, 977))
        self.assertEqual(b10.id, (98, 977))

    def test_id_valid_param_dict(self):
        """Check dict as id"""
        b11 = Base({"98": 977})
        self.assertEqual(b11.id, {"98": 977})

    def test_id_valid_param_set(self):
        """Check set as id"""
        b12 = Base({"98", 977})
        self.assertEqual(b12.id, {"98", 977})

    def test_id_valid_param_float(self):
        """Check float as id"""
        b13 = Base(3.14)
        self.assertEqual(b13.id, 3.14)

    def test_id_valid_param_inf(self):
        """Check inf as id"""
        b14 = Base(float('inf'))
        self.assertEqual(b14.id, float('inf'))

    def test_id_valid_param_func(self):
        """Check inf as id"""
        b15 = Base(len)
        self.assertEqual(b15.id("Hi"), 2)

    def test_id_valid_isprivate(self):
        """Check whether __nb_objects is private"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

if __name__ == '__main__':
    unittest.main()
