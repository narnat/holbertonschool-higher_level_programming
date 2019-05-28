#!/usr/bin/python3
"""Matrix multiply module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiplies matrix"""
    if type(m_a) != list:
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    if type(m_b) != list:
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    if any(type(i) != list for i in m_a):
        raise ValueError("shapes ({},{}) and ({},{}) not aligned: 0 (dim 1)\
 != 2 (dim 0)".format(len(m_a), 0, len(m_b), len(m_b[0])))

    if any(type(i) != list for i in m_b):
        raise ValueError("shapes ({},{}) and ({},{}) not aligned: 2 (dim 1)\
 != 0 (dim 0)".format(len(m_a), len(m_a[0]), len(m_b), 0))

    if any(not i for i in m_a):
        raise ValueError("shapes ({},{}) and ({},{}) not aligned: 0 (dim 1)\
 != 2 (dim 0)".format(len(m_a), len(m_a[0]), len(m_b), len(m_b[0])))

    if any(not i for i in m_b):
        raise ValueError("shapes ({},{}) and ({},{}) not aligned: 2 (dim 1)\
 != 1 (dim 0)".format(len(m_a), len(m_a[0]), len(m_b), len(m_b[0])))

    if any(any(type(j) != int and type(j) != float for j in i) for i in m_a):
        raise TypeError("invalid data type for einsum")

    if any(any(type(j) != int and type(j) != float for j in i) for i in m_b):
        raise TypeError("invalid data type for einsum")

    l_a = len(m_a[0])
    if any(len(row) != l_a for row in m_a):
        raise TypeError("setting an array element with a sequence.")

    l_b = len(m_b[0])
    if any(len(row) != l_b for row in m_b):
        raise TypeError("setting an array element with a sequence.")

    if len(m_a[0]) != len(m_b):
        raise ValueError("shapes ({0},{1}) and ({2},{3}) not aligned: {1}\
 (dim 1) != {2} (dim 0)".format(len(m_a), len(m_a[0]), len(m_b), len(m_b[0])))
    return numpy.matmul(m_a, m_b)
