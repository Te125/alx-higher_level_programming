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
        """ Create an instance of the rectangle class """
        r = Rectangle(3, 2)
        """ Define the captured output """
        captured_output = StringIO()
        """ Capture the sys std output """
        sys.stdout = captured_output
        """ Define the display method """
        r.display()
        """ Adjust sys output """
        sys.stdout = sys.__stdout__
        """ Copare the captured output with the # """
        self.assertEqual(captured_output.getvalue(), "###\n###\n")

    def test_str_method(self):
        """ Create an instance of Rectangle """
        rect = Rectangle(4, 3, 1, 2, 7)
        """ Get the string representation """
        str_representation = str(rect)
        """ Define the expected string representation """
        expected_str = "[Rectangle] (7) 1/2 - 4/3"
        """ Check if the generated string matches the expected string """
        self.assertEqual(str_representation, expected_str)

    def test_area_calculation(self):
        """ Create an instance of Rectangle with known dimensions """
        rect = Rectangle(4, 6)
        """ Calculate the area and check if it matches the expected result """
        self.assertEqual(rect.area(), 24)


if __name__ == '__main__':
    unittest.main()
