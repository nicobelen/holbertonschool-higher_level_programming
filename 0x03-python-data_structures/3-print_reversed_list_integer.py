#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    listlen = len(my_list)

    if listlen != 0:
        for i in range(listlen):
            print("{:d}".format(my_list[i]))
