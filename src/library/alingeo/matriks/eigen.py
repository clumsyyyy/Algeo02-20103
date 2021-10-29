from sympy import *
import numpy as np
import sympy as sp
from sympy.solvers import solve, solveset, linsolve

# [Library Eigenvalues]

# brief: menghasilkan list berisi eigen values dari sebuah matriks
# param input: List yang sudah dikonversi menjadi bentuk objek Matrix modul sympy

def eigenValues(A): 
    x = Symbol('x')
    I = eye(len(A.row(0)))
    result = solve((x*I - A).det(), domain = S.Reals)
    return result[::-1] #balikan nilai eigenvalues terurut mengecil, x1 > x2 > x3 ...


# brief: menghasilkan eigenvectors dari sebuah matriks
# param input: matriks dua dimensi, ukuran bebas

def eigenVectors(A):
    result = sp.Matrix([])
    count = 0
    for x in eigenValues(A):
        # Bentuk persamaan matA*x=matB
        # matA => A - eigenValues*I 
        # matB => Matriks 0
        I = eye(len(A.row(0)))
        matA = A - x*I
        null = [0 for i in range (len(matA.row(0)))]
        matB = Matrix(len(matA.row(0)),1,null) # zeros(len(matA.row(0)),1)

        sol, params = matA.gauss_jordan_solve(matB)

        for p in range(len(params)):
            count +=1
            taus_zeroes = {tau:0 for tau in params}
            urutan = 0 
            for tau in params:
                if (urutan == p) :
                    taus_zeroes[tau] = 1
                urutan +=1
            sol_unique = sol.xreplace(taus_zeroes)
            result = result.col_insert(count,sol_unique)
    return (result)   

# def eigenVectors(matrix):
#     eigenValues = eigenValue(matrix)
#     result = [] 
#     for a in range(len(eigenValues)):
#         SymbolArray = []
#         idenMatrix = [[0 for i in range(len(matrix))] for i in range(len(matrix))]
#         for i in range(0, len(idenMatrix[0])):
#             idenMatrix[i][i] = eigenValues[a]

#         for i in range(0, len(idenMatrix[0])):
#             idenMatrix[i].append(0)
#             for j in range(0, len(idenMatrix[0]) - 1):
#                 idenMatrix[i][j] -= matrix[i][j]

#         for i in range(0, len(idenMatrix[0]) - 1):
#             SymbolArray.append(Symbol(chr(i + 65)))


#         ansSet = linsolve(sp.Matrix(idenMatrix), SymbolArray)

#         ruangVektor = [[0 for j in range(len(SymbolArray))] for i in range (len(SymbolArray) - 1)]
#         for i in range(len(ruangVektor) + 1):
#             count = 0
#             for char in SymbolArray[1:]:
#                 if (str(char) in str(ansSet.args[0][i])):
#                     ruangVektor[count][i] = (ansSet.args[0][i].subs(str(char), 1))
#                 else:
#                     ruangVektor[count][i] = 0
#                 count += 1
#         result += ruangVektor
#     return result
# # Kode Driver
# def driver():
#     #y = int(input())
#     #mat = [[0 for j in range(y)]for i in range(y)]
#     #for i in range(0, y):
#         #mat[i] = list(map(int, input().split()))

#     print(eigenValue([[-1,4,-2],[-3,4,0],[-3,1,3]]))
#     print(eigenVectors([[-1,4,-2],[-3,4,0],[-3,1,3]]))

# driver()