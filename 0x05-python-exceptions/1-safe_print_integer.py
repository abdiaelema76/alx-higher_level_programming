#!/usr/bin/python3

def safe_print_integer(value):
    """function that prints an integer with "{:d}".format().
    Args:
        value (int): the interger to bbe printed
    Returns:
        True if value has been correctly printed
        otherwise - False
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
