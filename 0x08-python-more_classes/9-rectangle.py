#!/usr/bin/python3
"""Creates class Rectangle"""


class Rectangle:
    """Defines Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes Rectangle instance"""
        self.width = width
        self.height = height
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
        """Prints the rectangle with the character #"""
        output = ""
        if self.__width == 0 or self.__height == 0:
            return output
        else:
            for _ in range(self.__height):
                for _ in range(self.__width):
                    output += str(self.print_symbol)
                output += "\n"
        return output[:-1]

    def __repr__(self):
        """Returns string representation for rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints message when a rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares 2 rectangles and returns the biggest"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns new rectangle instance"""
        __width = size
        __height = size
        return cls(size, size)
