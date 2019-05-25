"""Matrix multiply module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiplies matrix"""
    if type(m_a) != list:
        raise ValueError("matmul: Input operand 0 does not have enough\
 dimensions (has 0, gufunc core with\
 signature (n?,k),(k,m?)->(n?,m?) requires 1)")

    if type(m_b) != list:
        raise ValueError("matmul: Input operand 1 does not have enough\
 dimensions (has 0, gufunc core with\
 signature (n?,k),(k,m?)->(n?,m?) requires 1)")

    if any(type(i) != list for i in m_a):
        raise ValueError("matmul: Input operand 0 does not have enough\
 dimensions (has 0, gufunc core with signature\
 (n?,k),(k,m?)->(n?,m?) requires 1)")

    if any(type(i) != list for i in m_b):
        raise ValueError("matmul: Input operand 1 does not have enough\
 dimensions (has 0, gufunc core with signature\
 (n?,k),(k,m?)->(n?,m?) requires 1)")

    if any(not i for i in m_a):
        raise ValueError("matmul: Input operand 0 does not have enough\
 dimensions (has 0, gufunc core with\
 signature (n?,k),(k,m?)->(n?,m?) requires 1)")

    if any(not i for i in m_b):
        raise ValueError("matmul: Input operand 1 does not have enough\
 dimensions (has 0, gufunc core with\
 signature (n?,k),(k,m?)->(n?,m?) requires 1)")

    if any(any(type(j) != int and type(j) != float for j in i) for i in m_a):
        raise TypeError("ufunc 'matmul' did not contain a loop with signature \
matching types dtype('<U21') dtype('<U21') dtype('<U21')")

    if any(any(type(j) != int and type(j) != float for j in i) for i in m_b):
        raise TypeError("ufunc 'matmul' did not contain a loop with signature \
matching types dtype('<U21') dtype('<U21') dtype('<U21')")

    l_a = len(m_a[0])
    if any(len(row) != l_a for row in m_a):
        raise TypeError("ufunc 'matmul' not supported for the input types,\
 and the inputs could not be safely coerced to any\
 supported types according to the casting rule ''safe''")

    l_b = len(m_b[0])
    if any(len(row) != l_b for row in m_b):
        raise TypeError("ufunc 'matmul' not supported for the input types,\
 and the inputs could not be safely coerced to any\
 supported types according to the casting rule ''safe''")

    if len(m_a[0]) != len(m_b):
        raise ValueError("matmul: Input operand 1 has a mismatch in its core \
dimension 0, with gufunc signature (n?,k),(k,m?)->(n?,m?) \
(size {} is different from {})".format(len(m_b), len(m_a[0])))


    return numpy.matmul(m_a, m_b)

lazy_matrix_mul([[21, 3], [32, 2]], [[32, 2, 2], [32, 32, 32], [32,32 ,32]])
