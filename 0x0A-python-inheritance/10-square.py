#!/usr/bin/python3
class BaseGeometry:
    """comment 1"""

    def area(self):
        """BaseGeometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """define area"""
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
        """Returns widht and height of Rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Square"""

    def __init__(self, size):
        """define init"""
        super().__init__(size, size)
        super().integer_validator('size', size)
        self.__size = size
