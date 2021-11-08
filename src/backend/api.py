from connexion import request
from PIL import Image

def compress(body):
    """
    Compress the image with SVD.
    """
    print(body)
    file = request.files.get('imageFile').read()
    img = Image.open(file)
    return {
        "statusCode": 200,
        "body": "Compressed"
    }
