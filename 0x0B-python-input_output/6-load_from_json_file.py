#!/usr/bin/python3
""" function that creates an object from a json file """
import json


def load_from_json_file(filename):
    """ function definition """
    with open(filename, mode="r", encoding="utf-8") as file:
        """ opening and closing the file with read mode """
        data = json.load(file)
    return data
