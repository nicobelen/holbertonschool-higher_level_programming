#!/usr/bin/python3
"""Creates class Rectangle"""


class Rectangle:
    number_of_instances = 0

    """Defines Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes Rectangle instance"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Returns area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        output = f"{'#' * self.__width}"
        for _ in range(self.__height - 1):
            output += f"\n{'#' * self.__width}"
        return output

    def __repr__(self):
        """Returns string representation for rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints message when a rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
