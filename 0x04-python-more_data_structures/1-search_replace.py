#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    lenlist = len(my_list)

    for i in range(lenlist):
        if my_list[i] == search:
            new_list.remove(search)
            new_list.insert(i, replace)
    return new_list
