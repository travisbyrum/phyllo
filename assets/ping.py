# -*- coding: utf-8 -*-

"""
{{.Title}}.resources.ping
~~~~~~~~~~~~~~~~~~~~
{{.Title}} ping resource.

"""

from flask_restful import Resource


# pylint: disable=R0201
class PingResource(Resource):
    """Ping pong response resource."""

    endpoints = ['/ping']

    def get(self):
        """Create response to http ping request.

        .. :quickref: Ping response.

        **Example request**:

        .. sourcecode:: http

            GET /ping HTTP/1.1
            Host: example.com
            Accept: application/json, text/javascript

        **Example response**:

        .. sourcecode:: http

            HTTP/1.1 200 OK
            Vary: Accept
            Content-Type: text/javascript
            {
                "message": "pong"
            }

        :reqheader Accept: The response content type depends on
            :mailheader:`Accept` header
        :reqheader Authorization: Optional authentication token.
        :resheader Content-Type: this depends on :mailheader:`Accept`
            header of request
        :statuscode 200: No error
        """

        return {'message': 'pong'}, 200
