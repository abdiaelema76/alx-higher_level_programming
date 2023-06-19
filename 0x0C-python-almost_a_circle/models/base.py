#!/usr/bin/python

#Defining The Base Class
class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization
        Args:
            id (int): Identity of the new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
