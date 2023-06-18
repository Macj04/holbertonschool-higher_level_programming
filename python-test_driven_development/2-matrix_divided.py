#!/usr/bin/python3
''' Write a function that divides all elements of a matrix '''


def matrix_divided(matrix, div):
    ''' div matrix '''
    new_matrix = []
    message = 'matrix must be a matrix (list of lists) of integers/floats'
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(message)
            result = item / div
            new_row.append(round(result, 2))
        new_matrix.append(new_row)
    return new_matrix
