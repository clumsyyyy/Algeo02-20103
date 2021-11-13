from io import BytesIO
from time import perf_counter_ns
from connexion import request
from flask import send_file, make_response
from alingeo.imaging.compress import CompressSVD

PARAM_ERROR = {
    'message': 'Missing parameters',
    'details': 'imageFile should exist',
    'status': 400,
}

INVALID_PARAM = {
    'message': 'Invalid parameters',
    'details': '',
    'status': 400,
}

compress_obj = CompressSVD()

request_name = {
    'scale': {
        'required': False,
        'validator': lambda x: 0 < x <= 100,
        'error_msg': 'Scale should be integer in range (0, 100]',
        'result': lambda x: x / 100,
    },
    'eigenRatio': {
        'required': False,
        'rename': 'eigen_ratio',
        'validator': lambda x: 0 < x <= 1,
        'error_msg': 'Eigen ratio should be float in range (0, 1]',
    },
    'preserveAlpha': {
        'required': False,
        'rename': 'preserve_alpha',
    },
    'iteration': {
        'required': False,
        'validator': lambda x: 2 <= x <= 100,
        'error_msg': 'Iteration should be integer in range [2, 100]',
    }
}

def compress(body):
    """Compress the image with SVD.

    Args:
        body (dict): The request body.

    Returns:
        app (dict): The response.
    """
    fileReq = request.files.get('imageFile')

    # Validate request
    if fileReq is None:
        return PARAM_ERROR, 400

    # Sanitize, validate, and preprocess input
    req = {}
    for req_name, req_value in request_name.items():
        if (
            req_name in body and
            ('validator' not in req_value or
            req_value['validator'](body[req_name]))
        ):
                req_res_name = req_value['rename'] if 'rename' in req_value else req_name
                if 'result' in req_value:
                    req[req_res_name] = req_value['result'](body[req_name])
                else:
                    req[req_res_name] = body[req_name]
        elif req_value['required']:
            INVALID_PARAM['details'] = req_value['error_msg']
            return INVALID_PARAM, 400

    # Get the file in memory
    file = BytesIO()
    fileReq.save(file)
    file.seek(0)

    # Start timer and compress the file
    duration = perf_counter_ns()
    res, cmp_rat, format = compress_obj.compress(file, **req)
    format = format.lower()

    # Stop timer and get the duration in secs. Close the file.
    duration = (perf_counter_ns() - duration) * 0.000000001 # in seconds
    file.close()

    # Get the compression result in memory
    file = BytesIO()
    read_only = False
    try:
        res.save(file, format)
    except KeyError:
        read_only = True
    if read_only:
        isAlpha = True
        try:
            res.getbands().index('A')
        except ValueError:
            isAlpha = False
        if isAlpha:
            format = 'png'
        else:
            format = 'jpeg'
        res.save(file, format)

    file.seek(0)

    # Create the response and add header for compression time & ratio
    response = make_response(send_file(
        file,
        as_attachment=True,
        attachment_filename=f'compressed.{format}',
    ))
    response.headers['X-Compression-Time'] = duration
    response.headers['X-Compression-Rate'] = cmp_rat
    return response
