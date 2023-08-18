#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        print("Dictionary is None")
        return

    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        value = a_dictionary[key]
        print(f"{key}: {value}")
