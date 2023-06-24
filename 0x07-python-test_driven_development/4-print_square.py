#!/usr/bin/python3
"""
    This module contains print_square function which
    prints a square with character #
"""


def print_square(size):
    """
    This function creates a square using '#'. The size is
    determined by the integer passed into the function
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
