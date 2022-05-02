#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()

    lenlist = len(my_list) - 1

    for i in range(lenlist):
        print(my_list[i])
