#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for emlent in range(len(matrix)):
            for itm in range(len(matrix[emlent])):
                if itm != len(matrix[emlent]) - 1:
                    spacemax = ' '
                else:
                    spacemax = ''
                print("{:d}".format(matrix[emlent][itm]), end=spacemax)
            print()
