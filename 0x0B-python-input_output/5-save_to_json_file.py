#!/usr/bin/python3
"""A function that defines a JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """A function that writes an object to a text file using JSON format"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
