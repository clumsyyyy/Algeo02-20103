import numpy as np
import math
from PIL import Image
from alingeo.matriks.svd import SVDSolver

class CompressSVD(object):
    def __init__(self, backend=None, iteration=2):
        """Generate a CompressSVD object with it's initial config.

        If backend is None, it will try to import jax and use it if available.
        In case jax is not installed, use numpy instead as the backend.

        Args:
            backend (numpy.array, Optional): Backend to be used. Default is None.
            iteration (int, Optional): Number of iteration to be used. Default is 2.
        """
        if backend is None:
            try:
                import jax.numpy as jnp
                backend = jnp
            except ImportError:
                backend = np
        self._backend = backend
        self._svdSolver = SVDSolver(backend, iteration)

    @property
    def backend(self):
        return self._backend
    @backend.setter
    def backend(self, value):
        self._backend = value
        self._svdSolver.backend = value
    
    @property
    def iteration(self):
        return self._svdSolver.iteration
    @iteration.setter
    def iteration(self, value):
        self._svdSolver.iteration = value
    
    def compress(
            self,
            image_file,
            eigen_val=None,
            eigen_ratio=0.2,
            scale=1,
            preserve_alpha=True,
            iteration=2,
        ):
        """Compress an Image bytes with SVD algorithm.

        Image will be scaled by a factor of scale first before doing the compression.
        Alpha channel will not be compressed if preserve_alpha is True.

        Eigen values k to be used is calculated by following formula:
            k = min(m, n * BAND_LENGTH) * ratio
        Thus, compression ratio is calculated by following formula:
            cmp_ratio = ((m * k + k + k * n * BAND_LENGTH) / (m * n * BAND_LENGTH))
        Where m, n is h, w of the image and BAND_LENGTH is the number of layer the image has.

        In case alpha is preserved, BAND_LENGTH will ignore the alpha channel as its
        not compressed by the algorithm.

        Args:
            image_file (BytesIO): Image to be compressed.
            eigen_val (int, Optional): Number of eigen value to be used. Default is None.
            eigen_ratio (float, Optional): Ratio (0,1] of eigen value to be used. Default is 0.2.
            scale (float, Optional): Scale (0, 1] of the image to be used. Default is 1.
            preserve_alpha (boolean, Optional): Preserve alpha channel. Default is True.

        Returns:
            finimg, cmp_ratio, format (Image, int, str): Compressed image, its compression ratio and format.
        """
        # Get PIL Image and it's original mode
        img_orig = Image.open(image_file)
        FORMAT = img_orig.format
        ORIG_MODE = img_orig.mode

        # Set iteration
        self.iteration = iteration

        # Scale image if needed
        if scale < 1:
            img_orig = img_orig.resize((
                math.ceil(img_orig.width*scale),
                math.ceil(img_orig.height*scale),
            ))
        
        # Do conversion to RGB/RGBA (except L and L with alpha variants)
        if img_orig.mode in ['P', 'PA'] and 'transparency' in img_orig.info:
          img_orig = img_orig.convert('RGBA')
        elif img_orig.mode not in ['L', 'LA', 'La', 'RGBA', 'RGBa', 'RGB']:
          img_orig = img_orig.convert('RGB')
        
        # Convert to matrix (H,W,B), normalize the value to 0..1
        img = self._backend.array(img_orig, dtype="float32")
        img *= (1 / 255)

        # Get metadata before calculation (alpha, band length, mat shape)
        IMG_SIZE = img.shape
        BAND_LENGTH = len(img_orig.mode)
        isAlpha = False
        if len(IMG_SIZE) > 2 and IMG_SIZE[2] in [2, 4]: # alpha: XA or XYZA
          isAlpha = True
          # Remove alpha band from calculation if alpha is preserved
          if preserve_alpha:
            BAND_LENGTH -= 1
            IMG_SIZE = (
                IMG_SIZE[0],
                IMG_SIZE[1],
                IMG_SIZE[2] - 1,
            )

        # Flatten image (except it's alpha if preserve_alphae)
        if isAlpha and preserve_alpha:
          imgd = img[:,:,:BAND_LENGTH]
        else:
          imgd = img
        imgd = imgd.reshape((
            IMG_SIZE[0],
            IMG_SIZE[1]*BAND_LENGTH
        ))

        # Calculate SVD
        U, sigma, V = self._svdSolver.calculate(imgd)

        # Calculate the reduced k
        if eigen_val:
            k = eigen_val
        else:
            k = math.ceil(min(IMG_SIZE[0], IMG_SIZE[1]*BAND_LENGTH) * eigen_ratio)
        
        # Calculate compression ratio
        CMP_RATIO = (
            (IMG_SIZE[0]*k + k + k*IMG_SIZE[1]*BAND_LENGTH)
            / (IMG_SIZE[0]*IMG_SIZE[1]*BAND_LENGTH)
        )

        # Reduce SVD into k-rank and reshape it back to (H,W,B) except alpha
        reimgd = self._backend.matmul(
            U[:,:k],
            self._backend.matmul(
                self._backend.diag(
                    sigma[:k],
                ),
                V[:k,:],
            ),
        ).reshape(IMG_SIZE)

        # Put it back in original img (with alpha, if preserve_alpha is True)
        if isAlpha and preserve_alpha:
            reimgd = self.backend.append(
                reimgd,
                img[:,:,BAND_LENGTH].reshape((
                    IMG_SIZE[0], IMG_SIZE[1], 1,
                )),
                axis=2,
            )

        # Clamp into 0..1 and multiply by 255, set as numpy array uint8
        reimgd = np.array(reimgd.clip(0, 1) * 255, dtype="uint8")

        # Make it as PIL Image with the original (after convert) image mode
        finimg = Image.fromarray(reimgd, mode=img_orig.mode)

        # Convert it back to original (before convert) image mode if converted
        # Will revert if it's not supported
        if img_orig.mode != ORIG_MODE:
            finimg = finimg.convert(ORIG_MODE)

        return finimg, CMP_RATIO, FORMAT
