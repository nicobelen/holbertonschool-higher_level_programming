#!/usr/bin/python3
"""Initializes square instance"""


class Square:
    """Defines square"""
    def __init__(self, size=0):
        """Initializes square instance"""
        self.__size = size

    @property
    def size(self):
        """retrieves size of square"""
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
        """Returns area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
