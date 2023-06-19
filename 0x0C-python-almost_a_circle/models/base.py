#!/usr/bin/python

import json
import csv
import turtle

"" Defining The Base Class""
class Base:
    ""Initialization of Base Class""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects
