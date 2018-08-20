# -*- coding: utf-8 -*-

"""
{{.Title}}.common
~~~~~~~~~~
Common api functions and utilities.

"""

import sys

from flask import current_app
from flask.signals import got_request_exception
from flask_restful import Api
from flask_restful.utils import http_status_message
from werkzeug.datastructures import Headers
from werkzeug.exceptions import HTTPException


# pylint: disable=W0212
def _create_error_out(api_exception):
    got_request_exception.send(
        current_app._get_current_object(),
        exception=api_exception
    )

    headers = Headers()
    if isinstance(api_exception, HTTPException):
        status_code = api_exception.code
        msg = getattr(
            api_exception,
            'description',
            http_status_message(status_code)
        )
        headers = api_exception.get_response().headers
    else:
        status_code = 500
        msg = http_status_message(status_code)

    remove_headers = ('Content-Length',)

    for header in remove_headers:
        headers.pop(header, None)

    if status_code and status_code >= 500:
        exc_info = sys.exc_info()
        current_app.log_exception(exc_info)

    error_out = {
        'error': {
            'message': msg,
            'name': type(api_exception).__name__
        },
        'status': status_code,
        'success': False
    }

    return error_out, status_code, headers


# pylint: disable=W0221,W0212
class CustomApi(Api):
    """Api object inheriting from :class:`flask_restful.Api`."""

    def handle_error(self, api_exception):
        """Error handler for the API transforms a raised exception into a Flask
        response, with the appropriate HTTP status code and body.  Overwritten
        method from `flask_restful`.

        :param api_exception: Raised Exception object
        :type api_exception: Exception
        """

        error_out, status_code, headers = _create_error_out(api_exception)

        if status_code == 406 and self.default_mediatype is None:
            supported_mediatypes = list(self.representations.keys())

            if supported_mediatypes:
                fallback_mediatype = next(iter(supported_mediatypes))
            else:
                fallback_mediatype = 'text/plain'

            resp = self.make_response(
                error_out,
                status_code,
                headers,
                fallback_mediatype=fallback_mediatype
            )
        else:
            resp = self.make_response(error_out, status_code, headers)

        if status_code == 401:
            resp = self.unauthorized(resp)

        return resp
