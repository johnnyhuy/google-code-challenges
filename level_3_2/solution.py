from fractions import Fraction
from functools import reduce

def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def least_common_multiple(a, b):
    return a * b // greatest_common_divisor(a, b)

def convert_to_probabilities(matrix):
    number_of_states = len(matrix)
    terminal_states = []
    
    for state, row in enumerate(matrix):
        row_sum = sum(row)

        if row_sum == 0:
            terminal_states.append(state)
            continue
        for transition in range(number_of_states):
            matrix[state][transition] = Fraction(matrix[state][transition], row_sum)

    return terminal_states

def create_identity_matrix(size):
    identity_matrix = []

    for i in range(size):
        row = [1 if i == j else 0 for j in range(size)]
        identity_matrix.append(row)

    return identity_matrix

def subtract_matrices(matrix1, matrix2):
    size = len(matrix1)
    result_matrix = [[matrix1[i][j] - matrix2[i][j] for j in range(size)] for i in range(size)]

    return result_matrix

def invert_matrix(matrix):
    size = len(matrix)
    inverted_matrix = create_identity_matrix(size)

    for index in range(size):
        denominator = matrix[index][index]

        for j in range(size):
            matrix[index][j] /= denominator
            inverted_matrix[index][j] /= denominator

        for j in range(size):
            if index != j:
                coef = matrix[j][index]
                for k in range(size):
                    matrix[j][k] -= coef * matrix[index][k]
                    inverted_matrix[j][k] -= coef * inverted_matrix[index][k]

    return inverted_matrix

def multiply_matrices(matrix1, matrix2):
    result_matrix = []

    for i in range(len(matrix1)):
        row = [sum(matrix1[i][k]*matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))]
        result_matrix.append(row)

    return result_matrix

def solution(matrix):
    terminal_states = convert_to_probabilities(matrix)
    non_terminal_states = [state for state in range(len(matrix)) if state not in terminal_states]
    Q_matrix = [[matrix[i][j] for j in non_terminal_states] for i in non_terminal_states]
    R_matrix = [[matrix[i][j] for j in terminal_states] for i in non_terminal_states]
    identity_matrix = create_identity_matrix(len(Q_matrix))
    I_minus_Q_matrix = subtract_matrices(identity_matrix, Q_matrix)
    F_matrix = invert_matrix(I_minus_Q_matrix)
    FR_matrix = multiply_matrices(F_matrix, R_matrix)
    denominators = [fraction.denominator for fraction in FR_matrix[0]]
    common_denominator = reduce(least_common_multiple, denominators)
    result = [fraction.numerator * common_denominator // fraction.denominator for fraction in FR_matrix[0]]
    result.append(common_denominator)

    return result
