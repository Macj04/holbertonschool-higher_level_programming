#!/usr/bin/python3
''' pascal trinangle '''


def pascal_triangle(n):
    ''' funtion '''
    triangle = []
    for i in range(n):
        power = 11 ** i
        string_power = str(power)
        triangle.append(string_power)
    return triangle
