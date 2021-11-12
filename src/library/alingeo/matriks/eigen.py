import numpy as np

class EigenSolver(object):
    def __init__(self, backend=np, iteration=2):
        self.backend = backend
        self.iteration = iteration

    def _orthogonalIteration(self, mat):
        m, n = mat.shape
        k = min(m, n)
        Q = self.backend.full((k,k), 0.5, dtype="float32")
        Q, R = self.backend.linalg.qr(Q)

        for _ in range(self.iteration):
            Z = self.backend.matmul(mat, Q)
            Q, R = self.backend.linalg.qr(Z)
        return Q, R

    def calcEigens(self, mat):
        """Calculate eigen vector and eigen value of a matrix.

        Args:
            mat (np.ndarray): Matrix to be calculated.

        Returns:
            EV, EL (np.ndarray, np.ndarray): Tuple of eigen vector and it's eigen value list.
        """
        Q, R = self._orthogonalIteration(mat)
        return Q, self.backend.diag(R)
