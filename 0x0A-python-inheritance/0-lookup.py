#!/usr/bin/python3
"""
    Function that returns the list of available attributes
    and methods of an object
"""


def lookup(obj):
    
    """
        Function looks out for all attributes and methods of an object
    """
    return dir(obj)
