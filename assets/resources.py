# -*- coding: utf-8 -*-

"""
{{.Title}}.resource
~~~~~~~~~~
Application resources and route definitions

"""

from flask import Blueprint, jsonify, make_response
from flask_restful import Resource

from {{.Title}}.common import CustomApi

from .ping import PingResource


{{.Title}}_blueprint = Blueprint('{{.Title}}_blueprint', __name__)
{{.Title}}_api = CustomApi({{.Title}}_blueprint)


API_RESOURCES = [PingResource]


@{{.Title}}_api.representation('application/json')
def output_json(data, status_code, headers=None):
    """Json api representation using the flask serializer instead of the 
    default provided through flask_restless.

    :param data: Request data to serialize.
    :type data: dict
    :param status_code: Http status code.
    :type status_code: int
    :param headers: Headers to be sent in response, defaults to None.
    :param headers: dict, optional
    :return: Json serialized output.
    :rtype: flask.Response
    """

    headers = headers or {}

    response = make_response(jsonify(data), status_code)
    response.headers.extend(headers)

    return response


for resource in API_RESOURCES:
    {{.Title}}_api.add_resource(resource, *resource.endpoints)


__all__ = ['api_blueprint']
