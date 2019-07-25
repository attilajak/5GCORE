# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.models.sm_context_create_error import SmContextCreateError  # noqa: E501
from swagger_server.models.sm_context_created_data import SmContextCreatedData  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSMContextsCollectionController(BaseTestCase):
    """SMContextsCollectionController integration test stubs"""

    def test_post_sm_contexts(self):
        """Test case for post_sm_contexts

        Create SM Context
        """
        body = Body()
        response = self.client.open(
            '/sm-contexts',
            method='POST',
            data=json.dumps(body),
            content_type='multipart/related')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
