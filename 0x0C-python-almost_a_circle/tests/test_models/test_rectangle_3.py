#!/usr/bin/python3
"""Test cases for Rectangle class, task 3"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass_validate(unittest.TestCase):

    """Test cases for ractangle, task 3"""

    """
****************************************
            String
****************************************
    """

    def tearDown(self):
        """Teardown"""
        Base.reset()

    def test_params_str_width(self):
        """Check str as parameter"""
        with self.assertRaises(TypeError):
            Rectangle("string", 32)

    def test_params_str_height(self):
        """Check str as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, "string")

    def test_params_str_x(self):
        """Check str as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, "string")

    def test_params_str_y(self):
        """Check str as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, "string")

    def test_params_str_width_err_msg(self):
        """Check str as parameter, error message"""
        try:
            Rectangle("string", 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_str_height_err_msg(self):
        """Check str as parameter, error message"""
        try:
            Rectangle(12, "String")
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_params_str_x_err_msg(self):
        """Check str as parameter, error message"""
        try:
            Rectangle(43, 32, "s")
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_str_y_err_msg(self):
        """Check str as parameter, error message"""
        try:
            Rectangle(43, 32, 3, "s")
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

            """
****************************************
            List
****************************************
            """

    def test_params_list_width(self):
        """Check list as parameter"""
        with self.assertRaises(TypeError):
            Rectangle([21], 32)

    def test_params_list_height(self):
        """Check list as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, [32])

    def test_params_list_x(self):
        """Check list as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, [1])

    def test_params_list_y(self):
        """Check list as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, [43])

    def test_params_list_width_err_msg(self):
        """Check list as parameter, error message"""
        try:
            Rectangle([234], 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_list_height_err_msg(self):
        """Check list as parameter, error message"""
        try:
            Rectangle(12, ["String"])
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_params_list_x_err_msg(self):
        """Check list as parameter, error message"""
        try:
            Rectangle(43, 32, ["s"])
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_list_y_err_msg(self):
        """Check list as parameter, error message"""
        try:
            Rectangle(43, 32, 3, ["s"])
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

            """
****************************************
            Tuple
****************************************
            """

    def test_params_tuple_width(self):
        """Check tuple as parameter"""
        with self.assertRaises(TypeError):
            Rectangle((21, 32), 32)

    def test_params_tuple_height(self):
        """Check tuple as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, (32, 443))

    def test_params_tuple_x(self):
        """Check tuple as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, (1, 54))

    def test_params_tuple_y(self):
        """Check tuple as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, (43, 24))

    def test_params_tuple_width_err_msg(self):
        """Check tuple as parameter, error message"""
        try:
            Rectangle((234, 32), 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_tuple_height_err_msg(self):
        """Check tuple as parameter, error message"""
        try:
            Rectangle(12, ("String", 32))
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_params_tuple_x_err_msg(self):
        """Check tuple as parameter, error message"""
        try:
            Rectangle(43, 32, ("s", 4))
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_tuple_y_err_msg(self):
        """Check tuple as parameter, error message"""
        try:
            Rectangle(43, 32, 3, ("s", 542))
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

            """
****************************************
            Dictionary
****************************************
            """

    def test_params_dict_width(self):
        """Check dict as parameter"""
        with self.assertRaises(TypeError):
            Rectangle({21: 32}, 32)

    def test_params_dict_height(self):
        """Check dict as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, {32: 443})

    def test_params_dict_x(self):
        """Check dict as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, {1: 54})

    def test_params_dict_y(self):
        """Check dict as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, {43: 24})

    def test_params_dict_width_err_msg(self):
        """Check dict as parameter, error message"""
        try:
            Rectangle({234: 32}, 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_dict_height_err_msg(self):
        """Check dict as parameter, error message"""
        try:
            Rectangle(12, {"String": 32})
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_params_dict_x_err_msg(self):
        """Check dict as parameter, error message"""
        try:
            Rectangle(43, 32, {"s": 4})
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_dict_y_err_msg(self):
        """Check dict as parameter, error message"""
        try:
            Rectangle(43, 32, 3, {"s": 542})
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

            """
****************************************
            None
****************************************
            """

    def test_params_none_width(self):
        """Check none as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(None, 32)

    def test_params_none_height(self):
        """Check none as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, None)

    def test_params_none_x(self):
        """Check none as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, None)

    def test_params_dict_none(self):
        """Check none as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, None)

    def test_params_none_width_err_msg(self):
        """Check none as parameter, error message"""
        try:
            Rectangle(None, 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_none_height_err_msg(self):
        """Check none as parameter, error message"""
        try:
            Rectangle(12, None)
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_params_none_x_err_msg(self):
        """Check none as parameter, error message"""
        try:
            Rectangle(43, 32, None)
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_none_y_err_msg(self):
        """Check none as parameter, error message"""
        try:
            Rectangle(43, 32, 3, None)
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

            """
****************************************
                 Set
****************************************
            """

    def test_params_set_width(self):
        """Check set as parameter"""
        with self.assertRaises(TypeError):
            Rectangle({21, 32}, 32)

    def test_params_set_height(self):
        """Check set as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, {32, 443})

    def test_params_set_x(self):
        """Check set as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, {1, 54})

    def test_params_set_y(self):
        """Check set as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, {43, 24})

    def test_params_set_width_err_msg(self):
        """Check set as parameter, error message"""
        try:
            Rectangle({234, 32}, 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_set_height_err_msg(self):
        """Check set as parameter, error message"""
        try:
            Rectangle(12, {"String", 32})
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_params_set_x_err_msg(self):
        """Check set as parameter, error message"""
        try:
            Rectangle(43, 32, {"s", 4})
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_set_y_err_msg(self):
        """Check set as parameter, error message"""
        try:
            Rectangle(43, 32, 3, {"s": 542})
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

            """
****************************************
                 Function
****************************************
            """

    def test_params_func_width(self):
        """Check function as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(len, 32)

    def test_params_func_height(self):
        """Check func as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, len)

    def test_params_func_x(self):
        """Check function as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, len)

    def test_params_func_y(self):
        """Check function as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, len)

    def test_params_func_width_err_msg(self):
        """Check function as parameter, error message"""
        try:
            Rectangle(len, 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_func_height_err_msg(self):
        """Check function as parameter, error message"""
        try:
            Rectangle(12, len)
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_params_func_x_err_msg(self):
        """Check function as parameter, error message"""
        try:
            Rectangle(43, 32, len)
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_func_y_err_msg(self):
        """Check function as parameter, error message"""
        try:
            Rectangle(43, 32, 3, len)
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")
