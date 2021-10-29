import numpy as np
import sympy as sp
from sympy import *
import eigen

A = sp.Matrix([[3,1,1],[-1,3,1]])

def leftSingular(A):
# Masukan berupa matriks
# Menentukan vektor singular kiri
# Hitung nilai-nilai eigen dari AA^T
# Rank(A) = k = banyaknya nilai-nilai eigen tidak nol dari AA^T
    AT = A.T
    return A*AT

def matrixU(A):
# Menentukan vektor-vektor eigen u1, u2, ..., um
# Koresponden dengan nilai eigen AA^T
# Setiap komponen vektornya dibagi dengan panjang vektor. Diperolehh matriks U]
    AAT = leftSingular(A)
    u = eigen.eigenVectors(AAT)
    result = sp.Matrix([])
    for i in range(len(u.col(0))):
        uNormalized = u.col(i).normalized()
        result = result.col_insert(i,uNormalized)
    return result

def rightSingular(A):
# Menentukan vektor singular kanan
# Hitung nilai-nilai eigen dari A^TA
# Kemudian menentukan nilai-nilai singularnya
    AT = A.T
    return AT*A

def matrixVTranspose(A):
# Menentukan vektor-vektor eigen v1, v2, ..., vn
# Koresponden dengan nilai eigen A^TA
# Setiap komponen vektornya dibagi dengan panjang vektor. Diperolehh matriks V
# matriks V kemudian ditranspose sehingga menjadi V^T
    ATA = rightSingular(A)
    v = eigen.eigenVectors(ATA)
    result = sp.Matrix([])
    for i in range(len(v.col(0))):
        uNormalized = v.col(i).normalized()
        result = result.col_insert(i,uNormalized)
    return result.T


def matrixS(A):
# Membentuk matriks S berukuran m x n
# Elemen diagonalnya adalah nilai-nilai singular dari matriks A disusun dari besar ke kecil
# Nilai singular di dalam S adalah akar pangkat dua dari nilai-nilai eigen yang tidak nol dari A^TA
    rightSingularEigen = eigen.eigenValues(rightSingular(A))
    l = []
    for i in rightSingularEigen:
        if i != 0:
            l += [sp.sqrt(i)]
    def f(i,j):
        if i == j:
            return l[i]
        else:
            return 0
    return (sp.Matrix(len(matrixU(A).row(0)),len(matrixVTranspose(A).col(0)),f))


def svd(A):
    return matrixU(A), matrixS(A), matrixVTranspose(A)

u, s, vt = svd(A)

print(u)
print(s)
print(vt)