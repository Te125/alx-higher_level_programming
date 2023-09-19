#!/usr/bin/python3
""" unittest test for rectangle """

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    
    def test_initialization(self):
        """ Create an instance of Rectangle """
        rect = Rectangle(4, 6, 2, 3, 1)
        
        """ Check if attributes were initialized correctly """
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_invalid_width(self):
        """ Attempt to create a Rectangle with an invalid width """
        with self.assertRaises(ValueError):
            rect = Rectangle(-1, 6, 2, 3, 1)

    def test_invalid_height(self):
        """ Attempt to create a Rectangle with an invalid height """
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 0, 2, 3, 1)

    def test_invalid_x(self):
        """ Attempt to create a Rectangle with an invalid x-coordinate """
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 6, -2, 3, 1)

    def test_invalid_y(self):
        """ Attempt to create a Rectangle with an invalid y-coordinate """
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 6, 2, -3, 1)

if __name__ == '__main__':
    unittest.main()
