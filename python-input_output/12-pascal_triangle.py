#!/usr/bin/python3
''' trinangle '''


def pascal_triangle(n):
    ''' funtion '''
    row = []
    for i in range(n):
        x = 11**i
        str_x = str(x)
        row.append(str_x)
    return row
