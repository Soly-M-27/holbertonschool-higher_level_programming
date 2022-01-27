#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        a = [2, 5, 9, 11]
        self.assertEqual(max_integer(a), 11)

        a = [25, 7, 1, 13]
        self.assertEqual(max_integer(a), 25)

        a = [0, 60, 12, 5]
        self.assertEqual(max_integer(a), 60)

        a = [4, 29, 50, 12]
        self.assertEqual(max_integer(a), 50)

        a = [-1, -5, -9, -3]
        self.assertEqual(max_integer(a), -1)

        a = [24, 7, -3, 6]
        self.assertEqual(max_integer(a), 24)

        a = [1]
        self.assertEqual(max_integer(a), 1)

        a = []
        self.assertEqual(max_integer(a), None)


if __name__ == "__main__":
    unittest.main()
