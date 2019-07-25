# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.sm_context_create_data import SmContextCreateData  # noqa: F401,E501
from swagger_server import util


class Body(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, json_data=None, binary_data_n1_sm_message=None):  # noqa: E501
        """Body - a model defined in Swagger

        :param json_data: The json_data of this Body.  # noqa: E501
        :type json_data: SmContextCreateData
        :param binary_data_n1_sm_message: The binary_data_n1_sm_message of this Body.  # noqa: E501
        :type binary_data_n1_sm_message: str
        """
        self.swagger_types = {
            'json_data': SmContextCreateData,
            'binary_data_n1_sm_message': str
        }

        self.attribute_map = {
            'json_data': 'jsonData',
            'binary_data_n1_sm_message': 'binaryDataN1SmMessage'
        }
        self._json_data = json_data
        self._binary_data_n1_sm_message = binary_data_n1_sm_message

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body of this Body.  # noqa: E501
        :rtype: Body
        """
        return util.deserialize_model(dikt, cls)

    @property
    def json_data(self):
        """Gets the json_data of this Body.


        :return: The json_data of this Body.
        :rtype: SmContextCreateData
        """
        return self._json_data

    @json_data.setter
    def json_data(self, json_data):
        """Sets the json_data of this Body.


        :param json_data: The json_data of this Body.
        :type json_data: SmContextCreateData
        """

        self._json_data = json_data

    @property
    def binary_data_n1_sm_message(self):
        """Gets the binary_data_n1_sm_message of this Body.


        :return: The binary_data_n1_sm_message of this Body.
        :rtype: str
        """
        return self._binary_data_n1_sm_message

    @binary_data_n1_sm_message.setter
    def binary_data_n1_sm_message(self, binary_data_n1_sm_message):
        """Sets the binary_data_n1_sm_message of this Body.


        :param binary_data_n1_sm_message: The binary_data_n1_sm_message of this Body.
        :type binary_data_n1_sm_message: str
        """

        self._binary_data_n1_sm_message = binary_data_n1_sm_message