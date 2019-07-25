# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.models.body2 import Body2  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.models.sm_context_release_data import SmContextReleaseData  # noqa: E501
from swagger_server.models.sm_context_retrieve_data import SmContextRetrieveData  # noqa: E501
from swagger_server.models.sm_context_retrieved_data import SmContextRetrievedData  # noqa: E501
from swagger_server.models.sm_context_update_data import SmContextUpdateData  # noqa: E501
from swagger_server.models.sm_context_update_error import SmContextUpdateError  # noqa: E501
from swagger_server.models.sm_context_updated_data import SmContextUpdatedData  # noqa: E501
from swagger_server.test import BaseTestCase


class TestIndividualSMContextController(BaseTestCase):
    """IndividualSMContextController integration test stubs"""

    def test_release_sm_context(self):
        """Test case for release_sm_context

        Release SM Context
        """
        body = Body2()
        response = self.client.open(
            '/sm-contexts/{smContextRef}/release'.format(sm_context_ref='sm_context_ref_example'),
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
            '/sm-contexts/{smContextRef}/retrieve'.format(sm_context_ref='sm_context_ref_example'),
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
            '/sm-contexts/{smContextRef}/modify'.format(sm_context_ref='sm_context_ref_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
