from io import BytesIO
from time import perf_counter_ns
from connexion import request
from flask import send_file, make_response
from imghdr import what
from alingeo.imaging.compress import CompressSVD

PARAM_ERROR = {
    'message': 'Missing parameters',
    'details': 'imageFile, scale and eigenRatio should exist',
    'status': 400,
}

INVALID_PARAM = {
    'message': 'Invalid parameters',
    'details': '',
    'status': 400,
}

compress_obj = CompressSVD()

def compress(body):
    """Compress the image with SVD.

    Args:
        body (dict): The request body.

    Returns:
        app (dict): The response.
    """
    fileReq = request.files.get('imageFile')

    # Validate request
    if 'scale' not in body or 'eigenRatio' not in body or fileReq is None:
        return PARAM_ERROR, 400
    elif body['scale'] > 100 and body['scale'] < 1:
        INVALID_PARAM['details'] = 'Scale should be between 0 and 1'
        return INVALID_PARAM, 400
    elif body['eigenRatio'] > 1 and body['eigenRatio'] <= 0:
        INVALID_PARAM['details'] = 'eigenRatio should be between 0 and 1'
        return INVALID_PARAM, 400
    
    # Get the file in memory
    file = BytesIO()
    fileReq.save(file)
    BEFORE_SIZE = file.tell()
    file.seek(0)
    
    # Get the file format
    format = what(file)

    # Start timer and compress the file
    duration = perf_counter_ns()
    res = compress_obj.compress(file, ratio=body['eigenRatio'], scale=body['scale']/100)

    # Stop timer and get the duration. Close the file.
    duration = (perf_counter_ns() - duration) * 0.000000001 # in seconds
    file.close()

    # Get the compression result in memory
    file = BytesIO()
    res.save(file, format)
    AFTER_SIZE = file.tell()
    file.seek(0)

    # Create the response and add header for compression time & ratio
    response = make_response(send_file(
        file,
        as_attachment=True,
        attachment_filename=f'compressed.{format}',
    ))
    response.headers['X-Compression-Time'] = duration
    response.headers['X-Compression-Rate'] = AFTER_SIZE / BEFORE_SIZE
    return response
