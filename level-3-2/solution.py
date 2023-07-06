from fractions import Fraction
from functools import reduce
import copy

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def transform_matrix(m):
    states = len(m)
    terminal_states = []
    for i, row in enumerate(m):
        row_sum = sum(row)
        if row_sum == 0:
            terminal_states.append(i)
            continue
        for j in range(states):
            m[i][j] = Fraction(m[i][j], row_sum)
    return terminal_states

def get_identity_matrix(size):
    I = []
    for i in range(size):
        row = []
        for j in range(size):
            val = 1 if i == j else 0
            row.append(val)
        I.append(row)
    return I

def matrix_subtraction(A, B):
    size = len(A)
    result = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(A[i][j] - B[i][j])
        result.append(row)
    return result

def invert_matrix(m):
    size = len(m)
    inverted = get_identity_matrix(size)
    for i in range(size):
        denominator = m[i][i]
        for j in range(size):
            m[i][j] /= denominator
            inverted[i][j] /= denominator
        for j in range(size):
            if i != j:
                coef = m[j][i]
                for k in range(size):
                    m[j][k] -= coef * m[i][k]
                    inverted[j][k] -= coef * inverted[i][k]
    return inverted

def matrix_multiplication(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            val = sum(A[i][k]*B[k][j] for k in range(len(B)))
            row.append(val)
        result.append(row)
    return result

def solution(m):
    terminal_states = transform_matrix(m)
    non_terminal_states = [i for i in range(len(m)) if i not in terminal_states]
    Q = [[m[i][j] for j in non_terminal_states] for i in non_terminal_states]
    R = [[m[i][j] for j in terminal_states] for i in non_terminal_states]
    I = get_identity_matrix(len(Q))
    I_minus_Q = matrix_subtraction(I, Q)
    F = invert_matrix(I_minus_Q)
    FR = matrix_multiplication(F, R)
    denoms = [f.denominator for f in FR[0]]
    common_denom = reduce(lcm, denoms)
    result = [f.numerator * common_denom // f.denominator for f in FR[0]]
    result.append(common_denom)

    return result
