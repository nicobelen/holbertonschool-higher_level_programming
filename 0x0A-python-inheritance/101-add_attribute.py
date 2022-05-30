#!/usr/bin/python3
"""adds new obj to class"""


def add_attribute(obj, name, value):
    """add attribute if it's possible"""
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
