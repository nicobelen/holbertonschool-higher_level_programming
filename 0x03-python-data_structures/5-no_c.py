#!/usr/bin/python3
def no_c(my_string):
    lenstring = len(my_string)
    newstring = ""

    for i in range(lenstring):
        if my_string[i] == "c" or my_string[i] == "C":
            continue
        else:
            newstring += my_string[i]
    return newstring
