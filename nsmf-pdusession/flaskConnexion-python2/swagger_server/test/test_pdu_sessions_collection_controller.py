# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body3 import Body3  # noqa: E501
from swagger_server.models.pdu_session_create_data import PduSessionCreateData  # noqa: E501
from swagger_server.models.pdu_session_create_error import PduSessionCreateError  # noqa: E501
from swagger_server.models.pdu_session_created_data import PduSessionCreatedData  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPDUSessionsCollectionController(BaseTestCase):
    """PDUSessionsCollectionController integration test stubs"""

    def test_post_pdu_sessions(self):
        """Test case for post_pdu_sessions

        Create
        """
        body = Body3()
        response = self.client.open(
            '/pdu-sessions',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
