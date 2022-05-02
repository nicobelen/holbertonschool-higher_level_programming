#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = my_list.copy()

    lenlist = len(newlist) - 1

    if idx < 0:
        return newlist
    if idx > lenlist:
        return newlist
    else:
        newlist[idx] = element
        return newlist
