#!/usr/bin/python3
"""A funtion that checks if object is an instance of a class
or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """A function that returns true if object is an instance of a class
    or a class that the class inherits from
    """
    return (isinstance(obj, a_class))
