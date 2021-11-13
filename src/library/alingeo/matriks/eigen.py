import numpy as np

class EigenSolver(object):
    def __init__(self, backend=np, iteration=2):
        """Generate an EigenSolver object with it's initial config.
        
        Args:
            backend (np.ndarray, Optional): Backend to be used. Default is numpy.
            iteration (int, Optional): Number of iteration to be used. Default is 2.
        """
        self.backend = backend
        self.iteration = iteration

    def _orthogonalIteration(self, mat):
        """Do orthogonal iteration to calculate QR decomposition of a matrix.

        Orthogonal Iteration adalah metode versi lanjut yang memanfaatkan power iteration 
        sebagai salah satu metode di dalam Aljabar Linear untuk mengaproksimasi nilai eigen 
        dan vektor eigen dari suatu matriks secara simultan. 

        Idenya adalah setiap vektor eigen selalu ortogonal dengan vektor eigen dominan
        lainnya. Dengan power iteration, akan dicari vektor eigen yang ortoganal 
        dan dapat dijamin nilainya konvergen untuk vektor eigen lainnya.

        Iterasi dilakukan dengan mengalikan tiap vektor-vektor {q1,q2,...,qr} dan 
        nilainya disimpan pada matriks Q. Setiap operasi ini, akan dilakukan normalisasi
        pada tiap vektor mengggunakan dekomposisi QR.

        Dekomposisi QR adalah salah satu metode iteratif untuk mencari semua nilai 
        eigen dari suatu matriks. Misalkan A adalah matriks yang akan didekomposisi, 
        dengan metode QR, hasil dekomposisi dari matriks A adalah matriks Q dan matriks
        R. Matriks Q adalah matriks orthogonal dan matriks R adalah matriks segitiga
        atas. Matriks ortogonal adalah matriks yang jika dibalikkan(invers) akan 
        menghasilkan nilai transpose dari matriks tersebut. 

        Langkah-langkah (Algoritma):
        1. Misalkan matriks A adalah matriks dengan ukuran m x n yang akan dicari nilai 
        eigen dan vektor eigennya. Akan dibentuk suatu matriks Q_0(Q awal) yang ukurannya 
        adalah k x k dengan k=min(m,n). Elemen-elemen pada matriks Q_0 (q_i) rentangnya 
        0 <  qi < 1
        2. Akan dilakukan iterasi sebanyak i kali. Dibentuk suatu matriks Z_i yang merupakan
        hasil perkalian matriks A dengan matriks Q_i-1. Matriks Z_i akan didekomposisi
        dengan metode QR sehingga menghasilkan matriks Qi dan Ri. Iterasi dilakukan
        agar matriks Q_i dan R_i elemennya konvergen kepada suatu nilai yang nantinya 
        akan menjadi nilai eigen dan vektor eigen. Iterasi dapat ditentukan di awal 
        atau dapat diberikan batasan sehingga dapat berhenti ketika mencapai 
        galat(epsilon) yang ditetapkan.
        3. Setelah iterasi selesai, akan didapatkan matriks Q dan R. Kolom-kolom matriks Q
        adalah vektor eigen dari matriks A, sementara itu diagonal dari matriks R
        yang merupakan matriks segitiga atas adalah nilai eigen dari matriks A. 
        Tiap nilai eigen dan vektor eigen berkorespondensi pada kolom yang sama. 

        Args:
            mat (np.ndarray): Matrix to be calculated.
        Returns:
            Q, R (np.ndarray, np.ndarray): Tuple of Matrix Q and Matrix R as result of orthogonal iteration.
        """
        # Calculate size of mat
        m, n = mat.shape
        # Calculate the minimum size of mat to be used in Q
        k = min(m, n)
        # Initialize Q with size k x k and all elements are 0.5
        Q = self.backend.full((k,k), 0.5, dtype="float32")
        # First QR decomposition of Q
        Q, R = self.backend.linalg.qr(Q)
        # Do the iteration
        for _ in range(self.iteration):
            # Multiply Q with mat and store the result in Z
            Z = self.backend.matmul(mat, Q)
            # QR decomposition of matrix Z to get Q and R
            Q, R = self.backend.linalg.qr(Z)
        # Return Q and R
        return Q, R

    def calcEigens(self, mat):
        """Calculate eigen vector and eigen value of a matrix.

        Args:
            mat (np.ndarray): Matrix to be calculated.

        Returns:
            EV, EL (np.ndarray, np.ndarray): Tuple of eigen vector and it's eigen value list.
        """
        # Do the orthogonal iteration
        Q, R = self._orthogonalIteration(mat)
        # The column of Q is eigen vector, the diagonal of R is eigen value
        return Q, self.backend.diag(R)
