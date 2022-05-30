#!/usr/bin/python3
"""comment 1"""


class BaseGeometry:
    """BaseGeometry"""

    def area(self):
        """define area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """define integer validator"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return value
