#!/usr/bin/python3


def uniq_add(my_list=[]):
    empty_set = set()
    i = 0
    for element in my_list:
        if isinstance(element, int) and element not in empty_set:
            empty_set.add(element)
            i += element
    return i
