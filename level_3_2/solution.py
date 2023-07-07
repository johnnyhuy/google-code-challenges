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


def transposeMatrix(m):
    """Transpose a matrix"""
    return list(map(list, zip(*m)))


def getMatrixMinor(m, i, j):
    """Get the minor of a matrix element"""
    return [row[:j] + row[j + 1 :] for row in (m[:i] + m[i + 1 :])]


def getMatrixDeternminant(m):
    """Calculate the determinant of a matrix"""
    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += (
            ((-1) ** c) * m[0][c] * getMatrixDeternminant(getMatrixMinor(m, 0, c))
        )
    return determinant


def inverse_matrix(m):
    """Calculate the inverse of a matrix"""
    determinant = getMatrixDeternminant(m)
    # special case for 2x2 matrix:
    if len(m) == 2:
        return [
            [m[1][1] / determinant, -1 * m[0][1] / determinant],
            [-1 * m[1][0] / determinant, m[0][0] / determinant],
        ]

    # find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m, r, c)
            cofactorRow.append(((-1) ** (r + c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant
    return cofactors


def solution(m):
    # Get list of terminal states
    terminal_states = [i for i, row in enumerate(m) if sum(row) == 0]
    if not terminal_states:
        return [1] + [0] * (len(m) - 1) + [1]

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
    F = inverse_matrix(IQ)
    FR = matmult(F, R)

    # The probabilities are the first row of FR
    probabilities = FR[0]

    # Convert to the required output format
    denominator = reduce(lcm, [f.denominator for f in probabilities])
    probabilities = [f.numerator * denominator // f.denominator for f in probabilities]
    probabilities.append(denominator)

    return probabilities
