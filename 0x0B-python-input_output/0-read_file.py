#!/usr/bin/python3
import json
import sys


def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, sys.stdout)
