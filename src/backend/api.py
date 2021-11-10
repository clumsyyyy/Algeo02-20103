import io
from connexion import request
from flask import send_file

def compress(body):
    """
    Compress the image with SVD.
    """
    print(body)
    file = io.BytesIO()
    request.files.get('imageFile').save(file)
    file.seek(0)
    return send_file(file, as_attachment=True, attachment_filename='compressed.jpg')
