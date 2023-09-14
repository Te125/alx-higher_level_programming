#!/usr/bin/python3
""" Functio that returns true if the object is an insance of a class """


def inherits_from(obj, a_class):
    """ Defining class """
    return issubclass(type(obj), a_class) and type(obj) != a_class
