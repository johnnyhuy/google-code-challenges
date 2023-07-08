from fractions import Fraction
from functools import reduce


def lcm(a, b):
    """Compute the least common multiple of a and b"""
    return a * b // gcd(a, b)


def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b:
        a, b = b, a % b
    return a


def matmult(a, b):
    """Multiply two matrices"""
    zip_b = list(zip(*b))
    return [
        [sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b)) for col_b in zip_b]
        for row_a in a
    ]


def transpose_matrix(m):
    """Transpose a matrix"""
    return list(map(list, zip(*m)))


def get_matrix_minor(m, i, j):
    """Get the minor of a matrix element"""
    return [row[:j] + row[j + 1 :] for row in (m[:i] + m[i + 1 :])]


def get_matrix_determinant(m):
    """Calculate the determinant of a matrix"""
    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += (
            ((-1) ** c) * m[0][c] * get_matrix_determinant(get_matrix_minor(m, 0, c))
        )
    return determinant


def inverse_matrix(m):
    """Calculate the inverse of a matrix"""

    determinant = get_matrix_determinant(m)

    if determinant == 0:
        raise ValueError("Matrix is singular and cannot be inverted")

    # special case for 2x2 matrix:
    if len(m) == 2:
        return [
            [m[1][1] / determinant, -1 * m[0][1] / determinant],
            [-1 * m[1][0] / determinant, m[0][0] / determinant],
        ]

    # find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactor_row = []
        for c in range(len(m)):
            minor = get_matrix_minor(m, r, c)
            cofactor_row.append(((-1) ** (r + c)) * get_matrix_determinant(minor))
        cofactors.append(cofactor_row)
    cofactors = transpose_matrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant
    return cofactors


def solution(m):
    # Check if the matrix is square
    if len(m) != len(m[0]):
        return None

    # Get list of terminal states
    terminal_states = [i for i, row in enumerate(m) if sum(row) == 0]
    if not terminal_states:
        return [1] * len(m)

    # Convert the matrix to fractions
    for i, row in enumerate(m):
        s = sum(row)
        if s > 0:
            m[i] = [Fraction(n, s) for n in row]

    # Reorder the matrix
    states = terminal_states + [i for i in range(len(m)) if i not in terminal_states]
    m = [[m[i][j] for j in states] for i in states]

    # Split the matrix into Q and R
    n = len(terminal_states)
    Q = [row[n:] for row in m[n:]]
    R = [row[:n] for row in m[n:]]

    # Calculate FR = (I-Q)^-1 * R
    I = [[int(i == j) for j in range(len(Q))] for i in range(len(Q))]
    IQ = [[a - b for a, b in zip(I_row, Q_row)] for I_row, Q_row in zip(I, Q)]

    try:
        F = inverse_matrix(IQ)
    except ValueError as e:
        print(e)
        return None

    FR = matmult(F, R)

    # The probabilities are the first row of FR
    probabilities = FR[0]

    # Convert to the required output format
    denominator = reduce(lcm, [f.denominator for f in probabilities])
    probabilities = [f.numerator * denominator // f.denominator for f in probabilities]
    probabilities.append(denominator)

    return probabilities
