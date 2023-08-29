#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            elem_1 = my_list_1[i] if i < len(my_list_1) else 0
            elem_2 = my_list_2[i] if i < len(my_list_2) else 0
            if type(elem_1) in (int, float) and type(elem_2) in (int, float) and elem_2 != 0:
                new_list.append(elem_1 / elem_2)
            elif type(elem_1) not in (int, float) or type(elem_2) not in (int, float):
                print("wrong type")
                new_list.append(0)
            else:
                print("division by 0")
                new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        return new_list
