#!/usr/bin/python3
from encodings import utf_8


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
