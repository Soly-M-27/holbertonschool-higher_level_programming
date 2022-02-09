#!/usr/bin/python3
""" Module to test Rectangle class """

from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """ Class Rectangle """

    @classmethod
    def setUpClass(cls):
        """ Method to test init """
        cls.rect1 = Rectangle(5, 4)
        cls.rect2 = Rectangle(5, 4, 7)
        cls.rect3 = Rectangle(5, 4, 8, 9)

    def test_width(self):
        """ method to test width """
        self.assertEqual(self.rect1.width, 5)

    def test_height(self):
        """ method to test height """
        self.assertEqual(self.rect1.height, 4)

    def test_x(self):
        """ method to test x """
        self.assertEqual(self.rect1.height, 4)
        self.assertEqual(self.rect2.x, 7)

    def test_y(self):
        """ method to test y """
        self.assertEqual(self.rect1.height, 4)
        self.assertEqual(self.rect3.y, 9)

    def test_negative_width(self):
        """ method that tests if width is negative """
        self.assertEqual(self.rect1.height, 4)
        with self.assertRaises(ValueError) as cm:
            rectangle = Rectangle(-4, 6)

    def test_negative_height(self):
        """ method to test if height is negative """
        self.assertEqual(self.rect1.height, 4)
        with self.assertRaises(ValueError) as cm:
            rectangle = Rectangle(4, -7)

    def test_negative_x(self):
        """ method that tests if x is negative """
        self.assertEqual(self.rect1.height, 4)
        with self.assertRaises(ValueError) as cm:
            rectangle = Rectangle(6, 7, -9)

    def test_negative_y(self):
        """ method that tests if y is negative """
        self.assertEqual(self.rect1.height, 4)
        with self.assertRaises(ValueError) as cm:
            rectangle = Rectangle(6, 7, 9, -9)

    def test_int_in_width(self):
        """ method that tests if width is an int or not """
        self.assertEqual(self.rect1.width, 5)
        with self.assertRaises(TypeError) as cm:
            rectangle = Rectangle(6.1, 4)

    def test_int_in_height(self):
        """ method that tests if height is an int or not """
        self.assertEqual(self.rect1.height, 4)
        with self.assertRaises(TypeError) as cm:
            rectangle = Rectangle(5, 4.2)

    def test_int_in_x(self):
        """ method that tests if x is an int or not """
        self.assertEqual(self.rect1.height, 4)
        self.assertEqual(self.rect2.x, 7)
        with self.assertRaises(TypeError) as cm:
            rectangle = Rectangle(5, 4, 7.5)

    def test_int_in_y(self):
        """ method that tests if y is an int or not """
        self.assertEqual(self.rect1.height, 4)
        self.assertEqual(self.rect3.y, 9)
        with self.assertRaises(TypeError) as cm:
            rectangle = Rectangle(5, 4, 7, 9.6)
