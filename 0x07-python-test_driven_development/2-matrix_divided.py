#!/usr/bin/python3


def matrix_divided(matrix, div):
    """divides all elements of a matrix.
    Args:
        a: the matrix of integers.
        b: Integer to divide by.
    Raises:
        TypeError: if matrix is not a list of lists of integers or floats.
        TypeError: if each row of the matrix is not the same size.
        TypeError: if Div is not an integer or a float.
        ZeroDivisionError: if div is 0.
    Returns:
        List: list of lists containing divided matrix.
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(div) not in(int, float):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
