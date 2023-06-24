#!/usr/bin/python3

""" deines a function that multiplies two matrices"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returns the multiplication of two matrices."""

    return (np.matmul(m_a, m_b))
