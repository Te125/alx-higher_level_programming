#!/usr/bin/python3
""" function that returns te dictionary description with simple data """


def class_to_json(obj):
    """ function definition """
    json_data = {}
    """ loop through objects """
    for attr_name, attr_value in obj.__dict__.items():
        if isinstance(attr_value, (list, dict, str, int, bool)):
            """ check if attribute is in serials """
            json_data[attr_name] = attr_value
    return json_data
