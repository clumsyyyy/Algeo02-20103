import numpy as np
import math
from PIL import Image
from alingeo.matriks.svd import svdOrthogonalIteration

def compressSVD(imageFile, eigenVal=None, ratio=0.2):
    """Compress an Image bytes with SVD algorithm.

    Args:
        image (BytesIO): Image to be compressed.

    Returns:
        PIL Image: Compressed image.
    """
    img_orig = Image.open(imageFile).convert()
    img = np.array(img_orig, dtype="float64")
    img *= (1/255)
    IMG_SIZE = img.shape
    BAND_LENGTH = len(img_orig.mode)
    imgd = img.reshape((IMG_SIZE[0], IMG_SIZE[1]*BAND_LENGTH))
    U, sigma, V = svdOrthogonalIteration(imgd)
    if ratio:
        k = math.ceil(min(IMG_SIZE[0], IMG_SIZE[1]*BAND_LENGTH) * ratio)
    if eigenVal:
        k = eigenVal
    reimgd = np.dot(U[:,:k],np.dot(np.diag(sigma[:k]),V[:k,:])).reshape(IMG_SIZE)
    finimg = Image.fromarray((reimgd.clip(0,1) * 255).astype("uint8"))
    return finimg
