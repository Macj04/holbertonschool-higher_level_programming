#!/usr/bin/python3
''' Function that Write a string to a text file '''


def write_file(filename="", text=""):
    ''' write a file  '''
    with open(filename, 'w', encoding='utf-8') as f:
        lstr = f.write(text)
        return lstr
