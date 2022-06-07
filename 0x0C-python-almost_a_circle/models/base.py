#!/usr/bin/python3
"""class base"""


import json
from queue import Empty


class Base:
    """define class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instanziation of id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return json representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries is Empty:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
