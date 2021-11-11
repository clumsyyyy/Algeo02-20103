import numpy as np
import jax.numpy as jnp

def orthogonalIteration(A):
    m,n = A.shape
    k = min(m,n)
    Q = np.random.rand(k,k)
    Q, _ = jnp.linalg.qr(Q)

    for i in range(2):
        Z = A @ Q
        Q, R = jnp.linalg.qr(Z)
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
    singularValues = jnp.sqrt(jnp.diag(jnp.abs(R)))
    if m_A > n_A:
        U = Q
        VT=jnp.nan_to_num(jnp.linalg.inv(jnp.diag(singularValues)),copy=False) @ U.T @ A
    elif m_A < n_A:
        VT=Q.T
        U=A @ Q @ jnp.nan_to_num(jnp.linalg.inv(jnp.diag(singularValues)),copy=False)
    else: 
        U=Q.T
        VT=U
        singularValues=jnp.square(singularValues)
    return U, singularValues, VT