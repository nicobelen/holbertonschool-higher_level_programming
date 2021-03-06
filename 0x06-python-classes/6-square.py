#!/usr/bin/python3
"""Creates class Square"""


class Square:
    """Defines square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes square instance"""
        self.size = size
        self.position = position

    def area(self):
        """Returns size of square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Retrieves size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets square position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints square"""
        if self.__size == 0:
            print()
        else:
            position = self.position
            if position[1] > 0:
                for i in range(position[1]):
                    print()
            for i in range(self.__size):
                print(" " * position[0] + "#" * self.size)
