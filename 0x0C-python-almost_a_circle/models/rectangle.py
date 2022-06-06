#!/usr/bin/python3
"""class rectangle"""


from models.base import Base


class Rectangle(Base):
    """define class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Retrieves width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves x of Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves x of Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Prints the rectangle with the character #"""
        n = "\n" * self.__y
        s = " " * self.__x
        print(n, end="")
        for _ in range(self.__height):
            print(f"{s}", end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns data of the rectangle"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Updates values of the rectangle"""
        count = 0
        if args is not None and len(args) != 0:
            for arg in args:
                if count == 0:
                    self.id = args[0]
                if count == 1:
                    self.__width = args[1]
                if count == 2:
                    self.__height = args[2]
                if count == 3:
                    self.__x = args[3]
                if count == 4:
                    self.__y = args[4]
                count += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
