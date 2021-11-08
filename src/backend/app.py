import logging
import os
from contextlib import suppress

import connexion


def create_app(test_config=None):
    logging.getLogger().setLevel(logging.INFO)
    con_app = connexion.App(
        __name__,
        specification_dir='./',
        options={
            'swagger_url': '/doc/',
        },
        debug=True,
    )
    con_app.add_api('swagger.yml')
    app = con_app.app
    app.config.from_mapping(
        SECRET_KEY=os.getenv('APP_SECRET', 'dev'),
        JSON_SORT_KEYS=False,
        use_reloader=False,
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    with suppress(OSError):
        os.makedirs(app.instance_path)

    return app