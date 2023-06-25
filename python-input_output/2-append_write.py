#!/usr/bin/python3
''' Function that append a string at the end of a text file  '''


def append_write(filename="", text=""):
    ''' Function '''
    with open(filename, 'a', encoding='utf-8') as f:
        line = f.write(text)
        return line
