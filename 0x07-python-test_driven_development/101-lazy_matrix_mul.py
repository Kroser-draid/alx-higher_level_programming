#!/usr/bin/python3
"""
module to multiplie two matrix
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    documented
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list)for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    m_a_len = len(m_a[0])
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(row) != m_a_len:
            raise TypeError("each row of m_a must be of the same size")

    m_b_len = len(m_b[0])
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

        if len(row) != m_b_len:
            raise TypeError("each row of m_b must be of the same size")

        try:
            result = np.dot(m_a, m_b)
        except Exception:
            raise ValueError("m_a and m_b can't be multiplied")

    return result
