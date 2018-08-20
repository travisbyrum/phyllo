# -*- coding: utf-8 -*-

"""
{{.Title}}.config
~~~~~~~~~~
Application configuration objects.

"""

import os


class Config:
    """Default configuration for application.  This object is meant for
    consumption by `Flask <http://flask.pocoo.org/>`_.
    """

    POSTGRES_HOST = os.getenv('DB_HOST')
    POSTGRES_PORT = int(os.getenv('DB_PORT')) if os.getenv('DB_PORT') else None
    POSTGRES_USER = os.getenv('DB_USER', 'postgres')
    POSTGRES_PASS = os.getenv('DB_PASS', 'postgres')
    POSTGRES_DB = os.getenv('DB_PASS', 'postgres')

    SQLALCHEMY_DATABASE_URI = os.getenv(
        'SQLALCHEMY_DATABASE_URI',
        'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
            POSTGRES_USER,
            POSTGRES_PASS,
            POSTGRES_HOST,
            str(POSTGRES_PORT),
            POSTGRES_DB
        )
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SUPPORTED_LOCALES = ['en']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key.upper(), value)


class TestConfig(Config):
    """Application testing configuration."""

    ASSETS_DEBUG = True
    DEBUG = True
    JSONIFY_PRETTYPRINT_REGULAR = True
    TESTING = True
    WTF_CRSF_ENABLED = False
