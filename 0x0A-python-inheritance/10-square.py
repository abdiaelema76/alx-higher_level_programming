#!/usr/bin/python3
"""Defines a square class that inherits from 9-rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square class"""

    def __init__(self, size):
        """Initialization  a new square class
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
