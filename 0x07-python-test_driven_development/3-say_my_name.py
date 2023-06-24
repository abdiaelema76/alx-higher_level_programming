#!/usr/bin/python3
"""
    This module contains say_my_name function which outputs a
    formatted string with the user's name
"""


def say_my_name(first_name, last_name=""):
    """Function  that returns a formatted string with the user's name"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
