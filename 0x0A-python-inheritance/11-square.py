#!/usr/bin/python3
"""Class import"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""

    def __init__(self, size):
        """define init"""
        self.__size = self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """Returns area"""
        return (self.__size ** 2)

    def __str__(self):
        """Returns widht and height of Square"""
        return f"[Square] {self.__size}/{self.__size}"
