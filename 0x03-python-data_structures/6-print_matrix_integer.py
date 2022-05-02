#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    listlen = len(matrix)

    for i in range(listlen):
        for j in range(len(matrix[i])):
            if j != 0:
                print(" ", end="")
            print("{:d}".format(matrix[i][j]), end="")
        print()
