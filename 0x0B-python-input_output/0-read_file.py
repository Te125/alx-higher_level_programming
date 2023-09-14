#!/usr/bin/python3
""" Function that reads a text file """


def read_file(filename=""):
    """ Defining file to read """
    try:
        """ open and close file """
        with open(filename, mode="r", encoding="utf-8") as file:
            for line in file:
                """ Print contents of the file """
                print(line, end="")
    except FileNotFoundError:
        """ if file does not exist, pass """
        pass
