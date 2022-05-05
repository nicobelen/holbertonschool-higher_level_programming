#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dic = a_dictionary.copy()
    for i in new_dic:
        if a_dictionary[i] == value:
            del a_dictionary[i]
    return a_dictionary
