# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.hsmf_update_data import HsmfUpdateData  # noqa: F401,E501
from swagger_server import util


class Body4(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, json_data=None, binary_data_n1_sm_info_from_ue=None, binary_data_unknown_n1_sm_info=None):  # noqa: E501
        """Body4 - a model defined in Swagger

        :param json_data: The json_data of this Body4.  # noqa: E501
        :type json_data: HsmfUpdateData
        :param binary_data_n1_sm_info_from_ue: The binary_data_n1_sm_info_from_ue of this Body4.  # noqa: E501
        :type binary_data_n1_sm_info_from_ue: str
        :param binary_data_unknown_n1_sm_info: The binary_data_unknown_n1_sm_info of this Body4.  # noqa: E501
        :type binary_data_unknown_n1_sm_info: str
        """
        self.swagger_types = {
            'json_data': HsmfUpdateData,
            'binary_data_n1_sm_info_from_ue': str,
            'binary_data_unknown_n1_sm_info': str
        }

        self.attribute_map = {
            'json_data': 'jsonData',
            'binary_data_n1_sm_info_from_ue': 'binaryDataN1SmInfoFromUe',
            'binary_data_unknown_n1_sm_info': 'binaryDataUnknownN1SmInfo'
        }
        self._json_data = json_data
        self._binary_data_n1_sm_info_from_ue = binary_data_n1_sm_info_from_ue
        self._binary_data_unknown_n1_sm_info = binary_data_unknown_n1_sm_info

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body_4 of this Body4.  # noqa: E501
        :rtype: Body4
        """
        return util.deserialize_model(dikt, cls)

    @property
    def json_data(self):
        """Gets the json_data of this Body4.


        :return: The json_data of this Body4.
        :rtype: HsmfUpdateData
        """
        return self._json_data

    @json_data.setter
    def json_data(self, json_data):
        """Sets the json_data of this Body4.


        :param json_data: The json_data of this Body4.
        :type json_data: HsmfUpdateData
        """

        self._json_data = json_data

    @property
    def binary_data_n1_sm_info_from_ue(self):
        """Gets the binary_data_n1_sm_info_from_ue of this Body4.


        :return: The binary_data_n1_sm_info_from_ue of this Body4.
        :rtype: str
        """
        return self._binary_data_n1_sm_info_from_ue

    @binary_data_n1_sm_info_from_ue.setter
    def binary_data_n1_sm_info_from_ue(self, binary_data_n1_sm_info_from_ue):
        """Sets the binary_data_n1_sm_info_from_ue of this Body4.


        :param binary_data_n1_sm_info_from_ue: The binary_data_n1_sm_info_from_ue of this Body4.
        :type binary_data_n1_sm_info_from_ue: str
        """

        self._binary_data_n1_sm_info_from_ue = binary_data_n1_sm_info_from_ue

    @property
    def binary_data_unknown_n1_sm_info(self):
        """Gets the binary_data_unknown_n1_sm_info of this Body4.


        :return: The binary_data_unknown_n1_sm_info of this Body4.
        :rtype: str
        """
        return self._binary_data_unknown_n1_sm_info

    @binary_data_unknown_n1_sm_info.setter
    def binary_data_unknown_n1_sm_info(self, binary_data_unknown_n1_sm_info):
        """Sets the binary_data_unknown_n1_sm_info of this Body4.


        :param binary_data_unknown_n1_sm_info: The binary_data_unknown_n1_sm_info of this Body4.
        :type binary_data_unknown_n1_sm_info: str
        """

        self._binary_data_unknown_n1_sm_info = binary_data_unknown_n1_sm_info
