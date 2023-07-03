#!/usr/bin/python3
"""Defines a Square class that inhrets from rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square class"""

    def __init__(self, size):
        """Initialization of  a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
