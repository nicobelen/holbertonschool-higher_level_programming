#!/usr/bin/python3
"""Comment 1"""


def inherits_from(obj, a_class):
    """define inherits from"""
    return (type(obj) != a_class and issubclass(type(obj), a_class))
