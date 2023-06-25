#!/usr/bin/python3
'''Create an object from a json file'''


import json


def load_from_json_file(filename):
    '''function'''
    with open(filename, 'r', encoding='utf-8') as f:
        string = f.read()
        obj = json.loads(string)
        return obj
