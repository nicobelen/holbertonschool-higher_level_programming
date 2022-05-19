#!/usr/bin/python3
"""Creates class Rectangle"""


class Rectangle:
    """Defines Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes Rectangle instance"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieves width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
