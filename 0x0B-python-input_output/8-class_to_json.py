#!/usr/bin/python3
""" function that returns te dictionary description with simple data """


def class_to_json(obj):
    """ function definition """
    return obj.__dict__
