#!/usr/bin/python3
''' Write the first class Base '''
import json
import os


class Base:
    '''Class'''
    __count = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__count += 1
            self.id = Base.__count

    @staticmethod
    def to_json_string(list_dicts):
        if list_dicts is None:
            return "[]"
        temp = json.dumps(list_dicts)
        return temp

    @classmethod
    def save_to_file(cls, list_objs):
        file = cls.__name__ + ".json"
        temp = []
        if list_objs:
            for obj in list_objs:
                temp.append(obj.to_dictionary())
        with open(file, "w") as f:
            f.write(Base.to_json_string(temp))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        temp = json.loads(json_string)
        return temp

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        elif cls.__name__ == 'Square':
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        file = cls.__name__ + ".json"
        objects = []
        dict_list = []
        if os.path.exists(file):
            with open(file, 'r') as f:
                content = f.read()
                dict_list = cls.from_json_string(content)
                for item in dict_list:
                    objects.append(cls.create(**item))
        return objects
