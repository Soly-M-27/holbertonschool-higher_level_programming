#!/usr/bin/python3
""" Module to test Square class """

from models.square import Square
import unittest


class TestSquare(unittest.TestCase):
    """ class TestSquare """

    @classmethod
    def setUpClass(cls):
        """ Method to test init """
        cls.sqr1 = Square(5)
        cls.sqr2 = Square(5, 6)
        cls.sqr3 = Square(5, 6, 2)

    def test_size_width(self):
        """ Method to test the size as width """
        self.assertEqual(self.sqr1.width, 5)

    def tets_size_height(self):
        """ Method to test the size as width """
        self.assertEqual(self.sqr1.height, 5)

    def test_x(self):
        """ Method to test x """
        self.assertEqual(self.sqr1.width, 5)
        self.assertEqual(self.sqr2.x, 6)

    def test_y(self):
        """ Method to test y """
        self.assertEqual(self.sqr1.height, 5)
        self.assertEqual(self.sqr3.y, 2)

    def test_negative_size_width(self):
        """ Method to test if size of width is negative """
        self.assertEqual(self.sqr1.width, 5)
        with self.assertRaises(ValueError) as cm:
            square = Square(-5)

    def test_negative_size_height(self):
        """ Method to test if size of width is negative """
        self.assertEqual(self.sqr1.height, 5)
        with self.assertRaises(ValueError) as cm:
            square = Square(-5)

    def test_negative_x(self):
        """ Method to test if size of width is negative """
        self.assertEqual(self.sqr2.x, 6)
        with self.assertRaises(ValueError) as cm:
            square = Square(-6)

    def test_negative_y(self):
        """ Method to test if size of width is negative """
        self.assertEqual(self.sqr3.y, 2)
        with self.assertRaises(ValueError) as cm:
            square = Square(-2)

    def test_int_size_width(self):
        """ Method to test if the size if an int or not """
        self.assertEqual(self.sqr1.width, 5)
        with self.assertRaises(TypeError) as cm:
            square = Square(5.3)

    def test_int_size_height(self):
        """ Method to test if the size if an int or not """
        self.assertEqual(self.sqr1.height, 5)
        with self.assertRaises(TypeError) as cm:
            square = Square(5.78)

    def test_int_x(self):
        """ Method to test if the size if an int or not """
        self.assertEqual(self.sqr2.x, 6)
        with self.assertRaises(TypeError) as cm:
            square = Square(6.2)

    def test_int_y(self):
        """ Method to test if the size if an int or not """
        self.assertEqual(self.sqr3.y, 2)
        with self.assertRaises(TypeError) as cm:
            square = Square(2.0)
