#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """prints an integer with "{:d}".format().
    Args:
        value (int): The integer to print.
    Returns:
        True if value has been correctly printed
        Otherwise - False and prints in stderr the error precede by Exception
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exceptiion: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
