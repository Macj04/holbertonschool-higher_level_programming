#!/usr/bin/python3
''' Function that return an object by json '''


import json


def from_json_string(my_str):
    '''Function'''
    return json.loads(my_str)
