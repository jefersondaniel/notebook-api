import os
import mongoengine
from app import app


def create_app(extra_config_settings={}):
    """
    Initialize Flask applicaton
    """

    app.config.from_object('app.startup.settings')
    app.config.update(extra_config_settings)

    # Load all blueprints with their manager commands, entities and views
    from app import core

    mongoengine.connect(
        app.config['DATABASE_NAME'],
        host=app.config['DATABASE_HOST'],
        port=app.config['DATABASE_PORT'],
        username=app.config['DATABASE_USER'],
        password=app.config['DATABASE_PASSWORD']
    )

    return app
