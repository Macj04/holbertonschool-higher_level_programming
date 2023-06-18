#!/usr/bin/python3
''' Function that print a square '''


def print_square(size):
    '''print a square'''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')


    square = '#' * size + '\n'
    square = square * size
    print(square)
