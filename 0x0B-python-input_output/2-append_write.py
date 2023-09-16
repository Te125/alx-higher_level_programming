#!/usr/bin/python3
""" Function that writes a string to a text file """


def append_write(filename="", text=""):
    """ Defining the function prototype """
    try:
        """ opening file in append mode """
        with open(filename, mode="a", encoding="utf-8") as file:
            num_chars_added = file.append(text)
            """ return the number of characters added """
        return num_chars_added
    except Exception:
        """ if error occurs while appending """
        return 0
