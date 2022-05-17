#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if isinstance(value, tuple(int, int)) is False:
            if tuple[0] < 1 or tuple[1] < 1 or len(value) != 2:
                raise TypeError("position must be a tuple of 2 positive integers")
            raise TypeError("position must be a tuple of 2 positive integers")


    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            position = self.position
            if position[1] > 0:
                for i in range(position[1]):
                    print("")
            for i in range(self.__size):
                print(" " * position[0] + "#" * self.size)
