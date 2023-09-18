#!/usr/bin/python3
""" script that adds all arguments """

import sys
import json


def save_to_json_file(my_obj, filename):
    """ function definition """
    with open(filename, mode="w", encoding="utf-8") as file:
        """ open file in write mode """
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """ load function definitio """
    try:
        """ open and close file and read with read mode """
        with open(filename, mode="r", encoding="utf-8") as file:
            """ return file load """
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        """ if file does not exist """
        return []


def main():
    """ main function definition """
    args_list = sys.argv[1:]
    """ load command line arguments """
    existing_data = load_from_json_file("add_item.json")
    """ load existing data from add_item.py if it exists """
    combined_list = existing_data + args_list
    """ combine the existing data from new arguments """
    save_to_json_file(combined_list, "add_item.json")
    """ save combined file to add_item.py """


if __name__ == "__main__":
    main()
