#!/usr/bin/python3
"""A fuction that defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """A function that inserts text after each line containing a given string in a file
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
