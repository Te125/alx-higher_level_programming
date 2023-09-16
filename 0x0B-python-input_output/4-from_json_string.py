#!/usr/bin/python3
""" Function that returns the object(python data structure) """
import json


def from_json_string(my_str):
    """ Defining the function and returns it """
    return json.loads(my_str)
