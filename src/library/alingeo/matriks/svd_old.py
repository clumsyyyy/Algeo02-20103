import sympy as sp
from sympy import Symbol, S
from sympy.simplify.simplify import simplify
from sympy.solvers import solve
from sympy.matrices import Matrix, eye, zeros
from sympy.solvers.pde import _simplify_variable_coeff
import eigen
import timeit

# Matriks untuk uji coba
A = Matrix([[3,1,1],[-1,3,1]])
B = Matrix(3,2,[1,1,0,1,-1,1])
C = Matrix(2,3,[3,2,2,2,3,-2])
X = Matrix(3,4,[1,1,0,1,0,0,0,1,1,1,0,0])
Y = Matrix(2,4,[1,0,1,0,0,1,0,1])

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
    result = zeros(len(matrixU(A).row(0)),len(matrixVTranspose(A).col(0)))
    m = 0
    for i in rightSingularEigen:
        if i != 0:
            result[m,m] = [sp.sqrt(i)]
        m+=1
    return result

def svd(A):
    return matrixU(A), matrixS(A), matrixVTranspose(A)


def driver(A):
    start = timeit.default_timer()

    #Your statements here
    u,s,vt = svd(A)
    result = u*s*vt
    print("Matriks: ")
    print(A)
    print("Matriks Singular Kiri: ")
    print(leftSingular(A))
    print("Nilai Eigen Matriks Singular Kiri: ")
    print(eigen.eigenValues(leftSingular(A)))
    print("Matriks Eigenvectors Singular Kiri: ")
    print(eigen.eigenVectors(leftSingular(A)))
    print("Matriks U:")
    print(u) 
    print("Nilai Eigen Matriks Singular Kanan: ")
    print(eigen.eigenValues(rightSingular(A)))
    print("Matriks Singular Kanan:")
    print(rightSingular(A))
    print("Matriks Eigenvectors Singular Kanan: ")
    print(eigen.eigenVectors(rightSingular(A)))
    print("Matriks S: ")
    print(s)
    print("Matrix VT: ")
    print(vt)
    print("Uji Matriks asal dengan perkalian U*S*VT:")
    print(A)
    print(result)
    print()
    
    stop = timeit.default_timer()

    print('Time: ', stop - start) 


driver(A)




