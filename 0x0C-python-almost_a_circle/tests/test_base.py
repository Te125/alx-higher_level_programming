#!/usr/bin/python3
""" unittest for base.py """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    
    def test_initialization_with_id(self):
        # Create an instance with a specified ID
        instance = Base(42)
        # Check if the instance's ID matches the specified ID
        self.assertEqual(instance.id, 42)
    
    def test_initialization_without_id(self):
        # Create multiple instances without specifying an ID
        instance1 = Base()
        instance2 = Base()
        instance3 = Base()
        # Check if each instance has a unique ID
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertNotEqual(instance1.id, instance3.id)
        self.assertNotEqual(instance2.id, instance3.id)

if __name__ == '__main__':
    unittest.main()
