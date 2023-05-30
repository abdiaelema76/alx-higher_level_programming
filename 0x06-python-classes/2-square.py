#!/usr/bin/python3

"""a module tha defines square based on 1-square.py"""

class Square:
    """A class that represents a square"""
    def __init__(self, size=0):
        """initialization of square class
        Args:
            size: represents size of a square defined
        Raises:
            TypeError: if size is not an Integer
            ValueError: if the size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError('size must be an Integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size 
