#!/usr/bin/python3
"""define a class square."""


class Square:
    """ Represents a square:"""
    def __init__(self, __size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = __size

    @property
    def size(self):
        """Get/set the current __size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Gives the area of the square"""
        return(self.__size * self.__size)
