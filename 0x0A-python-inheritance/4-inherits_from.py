#!/usr/bin/python3
"""A function that checks if object is an instance of a class that
inherited from the specified class or not
"""


def inherits_from(obj, a_class):
    """A function that returns true if object is an instance of a class that inherited
    from the specified class; otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
