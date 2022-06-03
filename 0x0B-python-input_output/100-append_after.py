#!/usr/bin/python3
"""function that inserts a line of text to a file, after each line
    containing a specific string """


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r', encoding='utf-8') as f:
        newtext = []
        lines = f.readlines()
        for line in lines:
            newtext += line
            if search_string in line:
                newtext += new_string
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(newtext)
