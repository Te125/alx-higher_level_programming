#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, number in enumerate(row):
            if i == len(row) - 1:
                print("{}".format(number))
            else:
                print("{} ".format(number), end="")

