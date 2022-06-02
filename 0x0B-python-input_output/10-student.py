#!/usr/bin/python3
"""Retrieves a dictionary representation of a Student instance"""


class Student:
    """Defines class"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """see comment up"""
        if attrs is None:
            return vars(self)
        return ({key: value for key, value in vars(self).items()
                 if key in attrs})
