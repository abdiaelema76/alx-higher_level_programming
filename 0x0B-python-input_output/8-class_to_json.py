#!/usr/bin/python3
"""A function that defines a Python class-to-JSON function"""


def class_to_json(obj):
    """A function that returns the dictionary representation of a simple data structure"""
    return obj.__dict__
