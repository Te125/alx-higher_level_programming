#!/usr/bin/python3
""" unittest test for rectangle """

import unittest
import sys
from io import StringIO
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

    def test_area_calculation(self):
        """ Create an instance of Rectangle with known dimensions """
        rect = Rectangle(4, 6, 2, 3, 1)
        
        """ Calculate the area and check if it matches the expected result """
        self.assertEqual(rect.area(), 24)

    def setUp(self):
        """ Redirect stdout to capture print output """
        self.stdout_backup = sys.stdout
        self.stdout_capture = StringIO()
        sys.stdout = self.stdout_capture

    def tearDown(self):
        """ Restore stdout """
        sys.stdout = self.stdout_backup

    def test_display_method(self):
        """ Create an instance of Rectangle """
        rect = Rectangle(4, 3)
        
        """ Capture the output of the display method """
        rect.display()
        displayed_output = self.stdout_capture.getvalue()
        
        """ Define the expected output """
        expected_output = "####\n####\n####\n"
        
        """ Check if the captured output matches the expected output """
        self.assertEqual(displayed_output, expected_output)


if __name__ == '__main__':
    unittest.main()
