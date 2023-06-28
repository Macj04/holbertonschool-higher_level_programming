#!/usr/bin/python3
'''Class Rectangle that inherits from Base'''
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self._width = self._validate_positive_integer(width, "width")
        self._height = self._validate_positive_integer(height, "height")
        self._x = self._validate_non_negative_integer(x, "x")
        self._y = self._validate_non_negative_integer(y, "y")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = self._validate_positive_integer(value, "width")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = self._validate_positive_integer(value, "height")

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = self._validate_non_negative_integer(value, "x")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = self._validate_non_negative_integer(value, "y")

    def area(self):
        return self._width * self._height

    def display(self):
        for _ in range(self._y):
            print()
        for _ in range(self._height):
            print(" " * self._x + "#" * self._width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self._x}/{self._y} - {self._width}/{self._height}"

    def update(self, *args, **kwargs):
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        return {
            "id": self.id,
            "width": self._width,
            "height": self._height,
            "x": self._x,
            "y": self._y,
        }

    def _validate_positive_integer(self, value, attribute):
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        if value <= 0:
            raise ValueError(f"{attribute} must be > 0")
        return value

    def _validate_non_negative_integer(self, value, attribute):
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute} must be >= 0")
        return value
