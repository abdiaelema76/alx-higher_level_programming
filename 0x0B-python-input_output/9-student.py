#!/usr/bin/python3
"""A function that defines a class Student"""


class Student:
    """Represents a student Class."""

    def __init__(self, first_name, last_name, age):
        """Initialization a new Student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A funcion that gets a dictionary representation of the Student"""
        return self.__dict__
