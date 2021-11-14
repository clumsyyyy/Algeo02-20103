import numpy as np
from alingeo.matriks.eigen import EigenSolver

class SVDSolver(object):
    def __init__(self, backend=np, iteration=2):
        """Generate an SVDSolver object with it's initial config.

        Args:
            backend (np.ndarray, Optimal): Backend to be used. Default is numpy.
            iteration (int, Optimal): Number of iteration to be used. Default is 2.
        """
        self._backend = backend
        self._eigenSolver = EigenSolver(backend, iteration)

    @property
    def backend(self):
        return self._backend
    @backend.setter
    def backend(self, value):
        self._backend = value
        self._eigenSolver.backend = value

    @property
    def iteration(self):
        return self._eigenSolver.iteration
    @iteration.setter
    def iteration(self, value):
        self._eigenSolver.iteration = value

    def calculate(self, A):
        """Calculate the SVD of the matrix and return it's SVD decomposition.

        The SVD decomposition of a matrix A = U * S * V^T.
        SVD memfaktorkan matriks A berukuran m x n menjadi matriks U, S, dan V
        sedemikian sehingga A = U x S x VT
        matriks U adalah matriks orthogonal m x m dibangun dari vektor eigen 
        matriks singular kiri (AA^T)
        matriks V adalah matriks orthogonal n x n dibangun dari vektor eigen 
        matriks singular kanan (A^TA)
        matriks S adalah matriks m x n yang elemen-elemen diagonal utamanya
        adalah nilai-nilai singular dari matriks A dan elemen lainnya 0
        Misalkan A adalah matriks m x n. Jika x1, x2, ..., xn adalah nilai-nilai
        eigen dari A^TA, maka s1 = sqrt(x1), s2 = sqrt(x2), ... sn = sqrt(xn)
        disebut nilai-nilai singular dari matriks A. Asumsi x1 >= x2 >= ... >= xn
        sehingga s1 >= s2 >= ... >= sn
        Fungsi SVD ini memanfaatkan orthogonal iteration. Matriks Q adalah matriks 
        yang akan diiterasi. Matriks Q ini juga akan menjadi salah satu matriks
        ortogonal antara matriks U atau matriks V bergantung dari kondisi berikut:
        Untuk matriks A berukuran m x n, 
        Jika m > n maka matriks Q adalah matriks U
        Jika m < n maka matriks Q adalah matriks V
        Jika m == n maka matriks Q adalah matriks U dan juga matriks V
        Jika salah satu nilai matriks singular baik kiri maupun kanan ditemukan, 
        dan nilai singularnya diketahui, maka dapat ditemukan pula matriks singular
        yang lainnya. Hal tersebut didapatkan menggunakan properti:
        A . V = U . S
        V^T = S^(-1) . U^T . A
        U = A . V . S^(-1)
        Langkah-langkah (Algoritma) :
        1. Misalkan matriks A adalah matriks berukuran m x n yang akan didekomposisi.
        Akan dicari terlebih dahulu matriks singular kiri atau kanannya berdasarkan 
        m dan n.
        2. Lakukan orthogonal iteration pada matriks singular yang telah ditetapkan
        sehinggga didapatkan matriks Q dan matriks R
        3. Tentukan matriks U, nilai singular, dan matriks VT berdasarkan penentuan
        awal dari ukuran matriks A.

        Args:
            mat (ndarray): The numpy matrix that you want to calculate.

        Returns:
            U, S, VT (ndarray, ndarray, ndarray): Tuple of U, S, and V^T
        """
        # Get matrix A shape, copy it to a var
        m_A, n_A = A.shape
        singularMatrix = A.copy()

        # Get the largest size, matmul with it's transpose
        if m_A < n_A:
            singularMatrix = self.backend.matmul(A, A.T)
        else: 
            singularMatrix = self.backend.matmul(A.T, A)

        # Get the eigenvalues and eigenvectors
        Q, singularValues = self._eigenSolver.calcEigens(singularMatrix)
        
        # Get the singular values (sqrt and absolute, in case negative eigval)
        singularValues = self.backend.sqrt(
            self.backend.abs(
                singularValues,
            ),
        )

        # Get the inverse of singular values (reciprocal).
        # In case of NaN, set them to 0 (nan_to_num)
        svInv = self.backend.nan_to_num(
            self.backend.diag(1 / singularValues),
            posinf=1,
            neginf=0,
        )
        # Set the U or V^T and calculate it's U or V^T, based on the m_A and n_A size
        if m_A < n_A:
            U = Q
            VT = self.backend.matmul(
                svInv,
                self.backend.matmul(
                    U.T,
                    A,
                ),
            )
        else:
            VT = Q.T
            U = self.backend.matmul(
                A,
                self.backend.matmul(
                    Q,
                    svInv,
                ),
            )

        return U, singularValues, VT
