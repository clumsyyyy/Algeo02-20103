import io
from connexion import request
from flask import send_file
from alingeo.imaging.compress import compressSVD

def compress(body):
    """
    Compress the image with SVD.
    """
    print(body)
    file = io.BytesIO()
    fileReq = request.files.get('imageFile')
    fileReq.save(file)
    file.seek(0)
    res = compressSVD(file)
    file.close()
    file = io.BytesIO()
    res.save(file, fileReq.mimetype[6:])
    res.save('test.jpg')
    file.seek(0)
    return send_file(file, as_attachment=True, attachment_filename=f'compressed.{fileReq.mimetype[6:]}')
