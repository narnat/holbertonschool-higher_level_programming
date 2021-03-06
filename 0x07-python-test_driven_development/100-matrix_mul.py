#!/usr/bin/python3
"""

Matrix multiply module

"""


def matrix_mul(m_a, m_b):
    """Multiplies matrix"""
    if type(m_a) != list:
        raise TypeError('m_a must be a list')

    if type(m_b) != list:
        raise TypeError('m_b must be a list')

    if any(type(i) != list for i in m_a):
        raise TypeError('m_a must be a list of lists')

    if any(type(i) != list for i in m_b):
        raise TypeError('m_b must be a list of lists')

    if any(not i for i in m_a):
        raise ValueError("m_a can't be empty")

    if any(not i for i in m_b):
        raise ValueError("m_b can't be empty")

    if any(any(type(j) != int and type(j) != float for j in i) for i in m_a):
        raise TypeError('m_a should contain only integers or floats')

    if any(any(type(j) != int and type(j) != float for j in i) for i in m_b):
        raise TypeError('m_b should contain only integers or floats')

    l_a = len(m_a[0])
    if any(len(row) != l_a for row in m_a):
        raise TypeError('each row of m_a must should be of the same size')

    l_b = len(m_b[0])
    if any(len(row) != l_b for row in m_b):
        raise TypeError('each row of m_b must should be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for row in range(len(m_b[0]))] for col in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
