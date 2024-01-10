#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    skare = []
    for lina in matrix:
        skare.append([c**2 for c in lina])
    return skare
