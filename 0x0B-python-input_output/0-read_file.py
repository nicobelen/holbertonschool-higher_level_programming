#!/usr/bin/python3
"""Function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """read the file"""
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
