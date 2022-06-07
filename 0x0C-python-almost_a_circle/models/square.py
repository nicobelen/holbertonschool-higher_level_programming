#!/usr/bin/python3
"""class square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """define square"""
    def __init__(self, size, x=0, y=0, id=None):
        """call super class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns data of the square"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}")

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates values of the rectangle"""
        count = 0
        if args is not None and len(args) != 0:
            for arg in args:
                if count == 0:
                    self.id = args[0]
                if count == 1:
                    self.size = args[1]
                if count == 2:
                    self.x = args[2]
                if count == 3:
                    self.y = args[3]
                count += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
