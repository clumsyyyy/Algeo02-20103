import numpy as np
from alingeo.matriks.eigen import EigenSolver

class SVDSolver(object):
    def __init__(self, backend=np, iteration=2):
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

        Args:
            mat (ndarray): The numpy matrix that you want to calculate.

        Returns:
            U, S, VT (ndarray, ndarray, ndarray): Tuple of U, S, and V^T
        """
        # Get matrix A shape, copy it to a var
        m_A, n_A = A.shape
        singularMatrix = A.copy()

        # Get the largest size, matmul with it's transpose
        if m_A > n_A:
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

        if m_A != n_A:
            # Get the inverse of singular values (reciprocal).
            # In case of NaN, set them to 0 (nan_to_num)
            svInv = self.backend.nan_to_num(
                self.backend.diag(1 / singularValues),
            )
            # Set the U or V^T and calculate it's U or V^T, based on the m_A and n_A size
            if m_A > n_A:
                U = Q
                VT = self.backend.matmul(
                    svInv,
                    self.backend.matmul(
                        U.T,
                        A,
                    ),
                )
            elif m_A < n_A:
                VT = Q.T
                U = self.backend.matmul(
                    A,
                    self.backend.matmul(
                        Q,
                        svInv,
                    ),
                )
        else:
            # If equal, U and VT should be equal to eigvec^T
            U = VT = Q.T
            # Singular values would be a square matrix
            singularValues = self.backend.square(singularValues)
        return U, singularValues, VT
