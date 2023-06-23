#!/usr/bin/python3
''' returns T/F if the object is an instance of the specified class '''


def is_same_class(obj, a_class):
    ''' Function '''
    if type(obj) is a_class:
        return True
    else:
        return False
