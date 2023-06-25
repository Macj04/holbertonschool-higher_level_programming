#!/usr/bin/python3
'''Class BaseGeometry based on task 6'''


class BaseGeometry:
    '''Class'''

    def area(self):
        '''Instance in building'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Value'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
