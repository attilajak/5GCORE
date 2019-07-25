# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.models.body2 import Body2  # noqa: E501
from swagger_server.models.body3 import Body3  # noqa: E501
from swagger_server.models.body4 import Body4  # noqa: E501
from swagger_server.models.hsmf_update_data import HsmfUpdateData  # noqa: E501
from swagger_server.models.hsmf_update_error import HsmfUpdateError  # noqa: E501
from swagger_server.models.hsmf_updated_data import HsmfUpdatedData  # noqa: E501
from swagger_server.models.pdu_session_create_data import PduSessionCreateData  # noqa: E501
from swagger_server.models.pdu_session_create_error import PduSessionCreateError  # noqa: E501
from swagger_server.models.pdu_session_created_data import PduSessionCreatedData  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.models.release_data import ReleaseData  # noqa: E501
from swagger_server.models.sm_context_create_error import SmContextCreateError  # noqa: E501
from swagger_server.models.sm_context_created_data import SmContextCreatedData  # noqa: E501
from swagger_server.models.sm_context_release_data import SmContextReleaseData  # noqa: E501
from swagger_server.models.sm_context_retrieve_data import SmContextRetrieveData  # noqa: E501
from swagger_server.models.sm_context_retrieved_data import SmContextRetrievedData  # noqa: E501
from swagger_server.models.sm_context_update_data import SmContextUpdateData  # noqa: E501
from swagger_server.models.sm_context_update_error import SmContextUpdateError  # noqa: E501
from swagger_server.models.sm_context_updated_data import SmContextUpdatedData  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_post_pdu_sessions(self):
        """Test case for post_pdu_sessions

        Create
        """
        body = Body3()
        response = self.client.open(
            '/nsmf-pdusession/v1/pdu-sessions',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_sm_contexts(self):
        """Test case for post_sm_contexts

        Create SM Context
        """
        body = Body()
        response = self.client.open(
            '/nsmf-pdusession/v1/sm-contexts',
            method='POST',
            data=json.dumps(body),
            content_type='multipart/related')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_release_pdu_session(self):
        """Test case for release_pdu_session

        Release
        """
        body = ReleaseData()
        response = self.client.open(
            '/nsmf-pdusession/v1/pdu-sessions/{pduSessionRef}/release'.format(pdu_session_ref='pdu_session_ref_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_release_sm_context(self):
        """Test case for release_sm_context

        Release SM Context
        """
        body = Body2()
        response = self.client.open(
            '/nsmf-pdusession/v1/sm-contexts/{smContextRef}/release'.format(sm_context_ref='sm_context_ref_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_sm_context(self):
        """Test case for retrieve_sm_context

        Retrieve SM Context
        """
        body = SmContextRetrieveData()
        response = self.client.open(
            '/nsmf-pdusession/v1/sm-contexts/{smContextRef}/retrieve'.format(sm_context_ref='sm_context_ref_example'),
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
            '/nsmf-pdusession/v1/pdu-sessions/{pduSessionRef}/modify'.format(pdu_session_ref='pdu_session_ref_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_sm_context(self):
        """Test case for update_sm_context

        Update SM Context
        """
        body = Body1()
        response = self.client.open(
            '/nsmf-pdusession/v1/sm-contexts/{smContextRef}/modify'.format(sm_context_ref='sm_context_ref_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
