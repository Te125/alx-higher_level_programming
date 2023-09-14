#!/usr/bin/python3
""" Class that inherits from list """


class MyList(list):
    """ Defining class list """
    def print_sorted(self):
        """ Initial class """
        sorted_list = sorted(self)
        """ print sorted list """
        print(sorted_list)
