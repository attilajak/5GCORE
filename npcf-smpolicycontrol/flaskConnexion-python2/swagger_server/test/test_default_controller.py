# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.models.sm_policy_context_data import SmPolicyContextData  # noqa: E501
from swagger_server.models.sm_policy_control import SmPolicyControl  # noqa: E501
from swagger_server.models.sm_policy_decision import SmPolicyDecision  # noqa: E501
from swagger_server.models.sm_policy_delete_data import SmPolicyDeleteData  # noqa: E501
from swagger_server.models.sm_policy_notification import SmPolicyNotification  # noqa: E501
from swagger_server.models.sm_policy_update_context_data import SmPolicyUpdateContextData  # noqa: E501
from swagger_server.models.termination_notification import TerminationNotification  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_sm_policies_post(self):
        """Test case for sm_policies_post

        
        """
        body = SmPolicyContextData()
        response = self.client.open(
            '/sm-policies',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sm_policies_sm_policy_id_delete_post(self):
        """Test case for sm_policies_sm_policy_id_delete_post

        
        """
        body = SmPolicyDeleteData()
        response = self.client.open(
            '/sm-policies/{smPolicyId}/delete'.format(sm_policy_id='sm_policy_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sm_policies_sm_policy_id_get(self):
        """Test case for sm_policies_sm_policy_id_get

        
        """
        response = self.client.open(
            '/sm-policies/{smPolicyId}'.format(sm_policy_id='sm_policy_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sm_policies_sm_policy_id_update_post(self):
        """Test case for sm_policies_sm_policy_id_update_post

        
        """
        body = SmPolicyUpdateContextData()
        response = self.client.open(
            '/sm-policies/{smPolicyId}/update'.format(sm_policy_id='sm_policy_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_smpolicynotify_terminate_post(self):
        """Test case for smpolicynotify_terminate_post

        
        """
        body = TerminationNotification()
        response = self.client.open(
            '/smpolicynotify/terminate',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_smpolicynotify_update_post(self):
        """Test case for smpolicynotify_update_post

        
        """
        body = SmPolicyNotification()
        response = self.client.open(
            '/smpolicynotify/update',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
