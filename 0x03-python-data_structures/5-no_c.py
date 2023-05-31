#!/usr/bin/env python3
def no_c(my_string):
    new_st = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_st += char
    return new_st
