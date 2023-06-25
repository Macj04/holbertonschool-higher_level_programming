#!/usr/bin/python3
''' Class Rectangle that inherits from task 7  '''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Class'''

    def __init__(self, width, height):
        '''class base'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
