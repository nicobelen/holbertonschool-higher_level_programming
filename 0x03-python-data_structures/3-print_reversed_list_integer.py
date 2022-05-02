#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lenlist = len(my_list)

    my_list.reverse()

    for i in range(lenlist):
        print(my_list[i])
