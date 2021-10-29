import sympy as sp
from sympy import *
import eigen


A = sp.Matrix([[3,1,1], [-1,3,1]])
AT = A.T
AAT = A*AT


print(eigen.eigenValues(AAT))

print(eigen.eigenVectors(AAT))

