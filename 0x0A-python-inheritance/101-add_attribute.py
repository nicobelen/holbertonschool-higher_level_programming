#!/usr/bin/python3
# class AddAtribute:
    
#     def __init__(self, obj, name, value):
#         self.obj = obj
#         self.name = name
#         self.value = value

def add_attribute(obj, name, value):
    atribute = setattr(obj, name, value)
    if not hasattr(atribute, name):
        raise TypeError("can't add new attribute")
    return atribute
