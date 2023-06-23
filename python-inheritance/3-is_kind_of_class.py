#!/usr/bin/python3
'''return T/F if the object is an instance'''


def is_kind_of_class(obj, a_class):
    is_instance = isinstance(obj, a_class)
    is_subclass = issubclass(type(obj), a_class)
    return is_instance or is_subclass
