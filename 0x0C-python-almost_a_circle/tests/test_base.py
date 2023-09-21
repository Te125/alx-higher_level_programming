#!/usr/bin/python3
""" unittest for base.py """
import unittest
from models.base import Base
import os
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    
    def test_initialization_with_id(self):
        """ Create an instance with a specified ID """
        instance = Base(42)
        """ Check if the instance's ID matches the specified ID """
        self.assertEqual(instance.id, 42)
    
    def test_initialization_without_id(self):
        """ Create multiple instances without specifying an ID """
        instance1 = Base()
        instance2 = Base()
        instance3 = Base()
        """ Check if each instance has a unique ID """
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertNotEqual(instance1.id, instance3.id)
        self.assertNotEqual(instance2.id, instance3.id)

    def test_to_json_string_with_empty_list(self):
        """ Check if json returns the string """
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_list_of_dicts(self):
        """ Takes the list of dictionaries and IDs """
        dicts = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        """ Compares strings """
        json_string = Base.to_json_string(dicts)
        self.assertEqual(json_string, '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]')

    def test_save_to_file_with_empty_list(self):
        """ Define rectangle file """
        Rectangle.save_to_file([])
        """ Check if path exists """
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", 'r') as file:
            """ Open file and check contents """
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_to_file_with_list_of_rectangles(self):
        """ Define a list of instances of rectangle"""
        r1 = Rectangle(10, 20)
        r2 = Rectangle(5, 15)
        Rectangle.save_to_file([r1, r2])
        """ Check path """
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", 'r') as file:
            """ overwrite contents of the file """
            content = file.read()
            expected = '[{"id": 1, "width": 10, "height": 20, "x": 0, "y": 0}, {"id": 2, "width": 5, "height": 15, "x": 0, "y": 0}]'
            """ Compare content and expected """
            self.assertEqual(content, expected)

    def test_save_to_file_with_list_of_squares(self):
        """ Define the list of instances of the square """
        s1 = Square(5)
        s2 = Square(8)
        Square.save_to_file([s1, s2])
        """ Check the path instance """
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", 'r') as file:
            content = file.read()
            expected = '[{"id": 1, "size": 5, "x": 0, "y": 0}, {"id": 2, "size": 8, "x": 0, "y": 0}]'
            self.assertEqual(content, expected)
        os.remove("Square.json")

    def tearDown(self):
        """ Check all the path instances in rectangle and square """
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_from_json_string_with_empty_string(self):
        """ Define the list of instances in an empty string """
        json_string = ""
        self.assertEqual(Base.from_json_string(json_string), [])

    def test_from_json_string_with_json_list(self):
        """ Check the instance ID with its objects """
        json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        result = Base.from_json_string(json_string)
        """ Check if the instaance specifies an object """
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['id'], 1)
        self.assertEqual(result[1]['name'], 'Jane')

    def test_create_method_with_rectangle(self):
        """ Create an instance with atributes """
        r_dict = {'id': 1, 'width': 5, 'height': 10}
        r = Rectangle.create(**r_dict)
        """ Check the provided attributes of the dictionary """
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)

    def test_create_method_with_square(self):
        """ Check the dictionary attributes """
        s_dict = {'id': 2, 'size': 7}
        s = Square.create(**s_dict)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 7)

    def test_create_method_with_invalid_class(self):
        """ Check the method for invalid class """
        d_dict = {'id': 3, 'name': 'Alice'}
        d = Base.create(**d_dict)
        self.assertIsNone(d)    

if __name__ == '__main__':
    unittest.main()
