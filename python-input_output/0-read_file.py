#!/usr/bin/python3
''' Function that read a text file (UTF8) and print it to stdout '''


def read_file(filename=""):
    '''Function'''
    f = open(filename, 'r', encoding='utf-8')
    for i in f:
        print(i, end='')
    f.close()
