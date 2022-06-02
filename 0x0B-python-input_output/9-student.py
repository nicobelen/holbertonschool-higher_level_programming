#!/usr/bin/python3
"""class Student"""


class Student:
    """Defines class"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dict representation of Student"""
        return vars(self)
