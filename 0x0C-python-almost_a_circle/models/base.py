#!/usr/bin/python3
"""class base"""


import json


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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Json string representation of list_objs"""
        if list_objs is None:
            text = "[]"
        else:
            dictlist = []
            for obj in list_objs:
                dictlist.append(obj.to_dictionary())
            text = cls.to_json_string(dictlist)
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(text)
