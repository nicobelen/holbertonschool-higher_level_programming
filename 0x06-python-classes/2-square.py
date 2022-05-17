#!/usr/bin/python3
"""Creates square class"""


class Square:
    """Defines square"""
    def __init__(self, size=0):
        """Initializes square instance"""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
