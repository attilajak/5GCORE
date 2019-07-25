# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body4 import Body4  # noqa: E501
from swagger_server.models.hsmf_update_data import HsmfUpdateData  # noqa: E501
from swagger_server.models.hsmf_update_error import HsmfUpdateError  # noqa: E501
from swagger_server.models.hsmf_updated_data import HsmfUpdatedData  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.models.release_data import ReleaseData  # noqa: E501
from swagger_server.test import BaseTestCase


class TestIndividualPDUSessionHSMFController(BaseTestCase):
    """IndividualPDUSessionHSMFController integration test stubs"""

    def test_release_pdu_session(self):
        """Test case for release_pdu_session

        Release
        """
        body = ReleaseData()
        response = self.client.open(
            '/pdu-sessions/{pduSessionRef}/release'.format(pdu_session_ref='pdu_session_ref_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_pdu_session(self):
        """Test case for update_pdu_session

        Update (initiated by V-SMF)
        """
        body = Body4()
        response = self.client.open(
            '/pdu-sessions/{pduSessionRef}/modify'.format(pdu_session_ref='pdu_session_ref_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
