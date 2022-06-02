#!/usr/bin/python3
"""function that inserts a line of text to a file, after each line
    containing a specific string """
def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'a+') as f:
        lines = f.readlines()
        for line in lines:
            if lines[line] == search_string:
                f.write("\n")
                f.write(new_string)
            else:
                continue
