import numpy as np
import sympy as sp
from sympy.solvers import solve, solveset
from sympy import Symbol, symbols, S

# [Library Eigenvalues]


# brief: menghasilkan matriks placeholder dari sebuah matriks
# format lambda.I - A
# param input: matriks dua dimensi, ukuran bebas

def placeHolder(matrix):
    x = Symbol('x')
    idenMatrix = [[0 for i in range(len(matrix))] for i in range(len(matrix))]
    for i in range(0, len(idenMatrix[0])):
        idenMatrix[i][i] = x

    for i in range(0, len(idenMatrix[0])):
        for j in range(0, len(idenMatrix[0])):
            idenMatrix[i][j] -= matrix[i][j]
    return idenMatrix


# brief: menghasilkan list berisi eigen values dari sebuah matriks
# param input: matriks dua dimensi, ukuran bebas

def eigenValue(matrix):
    return solve(sp.Matrix(placeHolder(matrix)).det(), domain = S.Reals)


# brief: menghasilkan eigenvectors dari sebuah matriks
# param input: matriks dua dimensi, ukuran bebas

def eigenVectors(matrix):
    eigenValues = eigenValue(matrix)
    print(eigenValues)
    for a in range(len(eigenValues)):
        idenMatrix = [[0 for i in range(len(matrix))] for i in range(len(matrix))]
        for i in range(0, len(idenMatrix[0])):
            idenMatrix[i][i] = eigenValues[a]

        for i in range(0, len(idenMatrix[0])):
            for j in range(0, len(idenMatrix[0])):
                idenMatrix[i][j] -= matrix[i][j]

        print(idenMatrix)
        homogenousMatrix = [0 for i in range(len(matrix))]
        print(homogenousMatrix)

        #TODO: SPL

def Inverse(matrix):
    cofactorMatrix = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix[0]))]
    temp = [[0 for j in range(len(matrix[0]) - 1)] for i in range(len(matrix[0]) - 1)]

    if sp.Matrix(matrix).det() == 0:
        return cofactorMatrix
    else:
        for h in range(0, len(matrix[0])):
            for i in range (0, len(matrix[0])):
                rowCount = 0
                for j in range(0, len(matrix[0])):
                    colCount = 0
                    for k in range(0, len(matrix[0])):
                        if (j != h and k != i):
                            temp[rowCount][colCount] = matrix[j][k]
                            colCount += 1
                    if (j != h):
                        rowCount += 1
                if ((h % 2 == 0 and i % 2 != 0) or (h % 2 != 0 and i % 2 == 0)):
                    cofactorMatrix[h][i] = -1 * sp.Matrix(temp).det()
                else:
                    cofactorMatrix[h][i] = sp.Matrix(temp).det()

    return cofactorMatrix

# Kode Driver
def driver():
    #y = int(input())
    #mat = [[0 for j in range(y)]for i in range(y)]
    #for i in range(0, y):
        #mat[i] = list(map(int, input().split()))
    print(eigenVectors([[3,0],[8,-1]]))

driver()