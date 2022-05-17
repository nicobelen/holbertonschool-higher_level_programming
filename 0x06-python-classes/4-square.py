#!/usr/bin/python3
"""Creates class Square"""


class Square:
    """Initializes square instance"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size of square"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns are of square"""
        return (self.__size * self.__size)
