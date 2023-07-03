#!/usr/bin/python3
"""Mylis inherits from the list class"""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        """prints  sorted list"""
        print(sorted(self))
