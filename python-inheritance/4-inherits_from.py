#!/usr/bin/python3
''' Function that return T/F '''


def inherits_from(obj, a_class):
    ''' Function that return '''
    is_instance = isinstance(obj, a_class)
    is_subclass = type(obj) != a_class
    return is_instance and is_subclass
