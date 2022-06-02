#!/usr/bin/python3
"""function that inserts a line of text to a file, after each line
    containing a specific string """


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r+') as f:
        lines = f.readlines()
        text = f.read()
        newtext = ""
        for line in lines:
            newtext += line
            if search_string in line:
                newtext += new_string
        f.truncate(0)
        f.writelines(newtext)
