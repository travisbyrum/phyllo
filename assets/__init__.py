# -*- coding: utf-8 -*-

"""
{{.Title}}
~~~~~
{{.Description}}

"""

from flask import Flask

from {{.Title}}.config import TestConfig
from {{.Title}}.extensions import db
from {{.Title}}.routes import {{.Title}}_blueprint


__version__ = '0.0.1'


def create_app(config=TestConfig, **kwargs):
    """Application factory.

    :param config: Application configuration object, defaults to TestConfig
    :type config: {{.Title}}.config, optional
    :return: {{.Title}} application.
    :rtype: flask.app.Flask
    """

    app = Flask(__name__)
    app.config.from_object(config)

    app = setup_application(app, **kwargs)

    return app


def setup_application(app, **kwargs):
    """Register application blueprints and extensions."""

    for name, value in kwargs.items():
        setattr(app, name, value)

    db.init_app(app)

    for blueprint in [{{.Title}}_blueprint]:
        app.register_blueprint(blueprint)

    return app
