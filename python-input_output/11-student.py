#!/usr/bin/python3
''' class Student that defines a student by task 10 '''


class Student:
    ''' class  '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Class '''
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        ''' Class '''
        for key, value in json.items():
            setattr(self, key, value)

    def from_json(cls, json):
        ''' Class '''
        return cls(**json)
