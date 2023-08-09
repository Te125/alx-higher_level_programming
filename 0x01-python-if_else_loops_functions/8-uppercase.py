#!/usr/bin/python3

def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print("{:s}".format(uppercase_char), end="")
        else:
            print("{:s}".format(char), end="")

            print()
