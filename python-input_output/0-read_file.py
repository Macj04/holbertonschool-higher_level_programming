#!/usr/bin/python3
''' Function that read and print a text file (UTF8) '''


def read_file(filename=""):
    ''' function read a file '''
    with open(filename, 'r', encoding='utf-8') as f:
        for i in f:
            print(i, end='')
