#!/usr/bin/python3

"""A module that  defines a square by: (based on 3-square.py)"""

class Square:
    """A class tha defines a square"""
    def __init__(self, size=0):
        """initialization of a square class
        Args:
            size: represents the size of quare defined
        Raises:
        TypeError: if size is not an integer
        ValueError: if size is not lss than zero
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

        def area(self):
            """Calculates area of the square"""
            return (self.__size ** 2)
