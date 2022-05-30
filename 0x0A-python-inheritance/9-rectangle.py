#!/usr/bin/python3
"""comment 1"""


class BaseGeometry:
    """BaseGeometry"""
    pass

    def area(self):
        """define area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """define integer validator"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """Rectangle"""

    def __init__(self, width, height):
        """define init"""
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of rectangle"""
        return (self.__width * self.__height)
    
    def __str__(self):
        """return size of width and height"""
        return f"[Rectangle] {self.__width}/{self.__height}"
