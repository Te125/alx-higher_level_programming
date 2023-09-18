#!/usr/bin/python3
""" Function that writes an object to a text file """
import json


def save_to_json_file(my_obj, filename):
    """ function definition """
    with open(filename, mode="w", encoding="utf-8") as file:
        """ open and close the file with the with,
        write to the file in write mode """
        json.dump(my_obj, file)
