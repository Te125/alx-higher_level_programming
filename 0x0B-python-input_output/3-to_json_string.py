#!/usr/bin/python3
""" Function that returns the json representation of an object """
import json


def to_json_string(my_obj):
    """ Defining the json object and returns the object """
    return json.dumps(my_obj)
