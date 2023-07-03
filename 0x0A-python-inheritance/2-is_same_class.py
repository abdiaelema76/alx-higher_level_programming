#!/usr/bin/python3
"""Checks if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """A function that returns true if object is an instance of the
    class, otherwise returns false
    """
    return (type(obj) == a_class)
