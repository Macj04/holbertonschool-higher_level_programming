#!/usr/bin/python3
''' write an object to a text file using json '''


import json


def save_to_json_file(my_obj, filename):
    '''Function'''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
        return f.tell()
