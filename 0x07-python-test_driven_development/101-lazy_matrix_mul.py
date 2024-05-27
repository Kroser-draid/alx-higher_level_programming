#!/usr/bin/python3
"""
Module for lazy_matrix_mul function
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.
    
    Args:
        m_a: A list of lists of integers or floats.
        m_b: A list of lists of integers or floats.
        
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    
    Raises:
        TypeError: If m_a or m_b is not a list of lists of integers/floats.
        ValueError: If m_a or m_b is empty or if they can't be multiplied.
    """
    # Validation of m_a
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")
    row_length_a = len(m_a[0])
    if not all(len(row) == row_length_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    
    # Validation of m_b
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")
    row_length_b = len(m_b[0])
    if not all(len(row) == row_length_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    
    # Check if the matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Perform the matrix multiplication using NumPy
    result = np.dot(m_a, m_b)
    
    return result.tolist()