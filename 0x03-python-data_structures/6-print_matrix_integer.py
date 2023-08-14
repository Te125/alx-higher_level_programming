#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        number = 0
        for j in i:
            number += 1
            if number == len(i):
                print("{}".format(j))
            else:
                print("{} ".format(j), end="")
    print()
