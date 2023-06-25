#!/usr/bin/python3
''' Class Square that inherits from task 10 '''


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' square Function '''

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):

        return self.__size ** 2

    def __str__(self):
        return str("[Square] {}/{}".format(self.__size, self.__size))
