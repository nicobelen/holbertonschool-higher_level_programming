#!/usr/bin/python3
"""class base"""


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
