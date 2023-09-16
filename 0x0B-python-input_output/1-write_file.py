#!/usr/bin/python3
""" Function that writes a string to a text file """


def write_file(filename="", text=""):
    """ Defining the function """
    try:
        """ opening the file in write mode """
        with open(filename, mode="w", encoding="utf-8") as file:
            num_chars_written = file.write(text)
            """ return number of characters written """
        return num_chars_written
    except Exception:
        """ if file doesnt exist """
        return 0
