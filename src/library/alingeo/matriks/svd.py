import numpy as np

def orthogonalIteration(A):
    m,n = A.shape
    k = min(m,n)
    Q = np.random.rand(k,k)
    Q, _ = np.linalg.qr(Q)

    for i in range(2):
        Z = A @ Q
        Q, R = np.linalg.qr(Z)
    return Q, R

def svdOrthogonalIteration(A):
    m_A, n_A = A.shape
    singularMatrix = A.copy()
    if m_A > n_A:
        singularMatrix = A @ A.T
    else: 
        singularMatrix = A.T @ A
    m_sM, n_sM = singularMatrix.shape
    Q, R = orthogonalIteration(singularMatrix)
    singularValues = np.sqrt(np.diag(np.abs(R)))
    if m_A > n_A:
        U = Q
        VT=np.nan_to_num(np.linalg.inv(np.diag(singularValues)),copy=False) @ U.T @ A
    elif m_A < n_A:
        VT=Q.T
        U=A @ Q @ np.nan_to_num(np.linalg.inv(np.diag(singularValues)),copy=False)
    else: 
        U=Q.T
        VT=U
        singularValues=np.square(singularValues)
    return U, singularValues, VT