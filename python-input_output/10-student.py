#!/usr/bin/python3
''' Class student that defines a student by task 9 '''


class Student:
    ''' class  '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''''''
        if attrs is None:
            return self.__dict__
        else:
            m = {}
            for x in attrs:
                if x in self.__dict__.keys():
                    m[x] = self.__dict__[x]
            return m
