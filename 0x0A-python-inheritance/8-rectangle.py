#!/usr/bin/python3
"""A class that Inherits from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that defines rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialization of a new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
