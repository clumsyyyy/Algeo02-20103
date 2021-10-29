from sympy import *
import numpy as np
import sympy as sp
from sympy.solvers import solve, solveset, linsolve


# [Library Eigenvalues]


# brief: menghasilkan list berisi eigen values dari sebuah matriks
# param input: matriks dua dimensi, ukuran bebas

def eigenValue(matrix):
    x = Symbol('x')
    i = np.eye(len(matrix))
    return solve(sp.Matrix(x*i - matrix).det(), domain = S.Reals)


# brief: menghasilkan eigenvectors dari sebuah matriks
# param input: matriks dua dimensi, ukuran bebas

def eigenVectors(matrix):
    eigenValues = eigenValue(matrix)
    for a in range(len(eigenValues)):
        SymbolArray = []
        idenMatrix = [[0 for i in range(len(matrix))] for i in range(len(matrix))]
        for i in range(0, len(idenMatrix[0])):
            idenMatrix[i][i] = eigenValues[a]

        for i in range(0, len(idenMatrix[0])):
            idenMatrix[i].append(0)
            for j in range(0, len(idenMatrix[0]) - 1):
                idenMatrix[i][j] -= matrix[i][j]

        for i in range(0, len(idenMatrix[0]) - 1):
            SymbolArray.append(Symbol(chr(i + 65)))


        ansSet = linsolve(sp.Matrix(idenMatrix), SymbolArray)

        ruangVektor = [[0 for j in range(len(SymbolArray))] for i in range (len(SymbolArray))]
        print(eigenValues[a])
        for i in range(len(idenMatrix)):
            count = 0
            for char in SymbolArray:
                if (str(char) in str(ansSet.args[0][i])):
                    print(ansSet.args[0][i].subs(str(char), 1))
                    ruangVektor[count][i] = (ansSet.args[0][i].subs(str(char), 1))
                else:
                    ruangVektor[count][i] = 0
                count += 1

        print(ruangVektor)


# Kode Driver
def driver():
    #y = int(input())
    #mat = [[0 for j in range(y)]for i in range(y)]
    #for i in range(0, y):
        #mat[i] = list(map(int, input().split()))
    eigenVectors([[3, -2, 0], [-2,3,0], [0,0,5]])

driver()