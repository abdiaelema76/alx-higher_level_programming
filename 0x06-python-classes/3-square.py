#!/usr/bin/python3

"""A module that defines a square by: (based on 2-square.py)"""

class Square:
    """Class that represent a square"""

    def __init__(self, size=0):
        """initialization of a new square
        Args:
            size: represents the size of square defined
        Raises:
            TypeError: if size is not an integer
            ValueError: f size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

        def Area(self):
            """Calculate area of the square
            Returns: the square of the size
            """
            return (self.__size ** 2)
