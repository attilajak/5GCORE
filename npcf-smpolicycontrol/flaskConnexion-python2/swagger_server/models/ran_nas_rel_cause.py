# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.model5_g_mm_cause import Model5GMmCause  # noqa: F401,E501
from swagger_server.models.model5_g_sm_cause import Model5GSmCause  # noqa: F401,E501
from swagger_server.models.ng_ap_cause import NgApCause  # noqa: F401,E501
from swagger_server import util


class RanNasRelCause(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ng_ap_cause=None, _5g_mm_cause=None, _5g_sm_cause=None):  # noqa: E501
        """RanNasRelCause - a model defined in Swagger

        :param ng_ap_cause: The ng_ap_cause of this RanNasRelCause.  # noqa: E501
        :type ng_ap_cause: NgApCause
        :param _5g_mm_cause: The _5g_mm_cause of this RanNasRelCause.  # noqa: E501
        :type _5g_mm_cause: Model5GMmCause
        :param _5g_sm_cause: The _5g_sm_cause of this RanNasRelCause.  # noqa: E501
        :type _5g_sm_cause: Model5GSmCause
        """
        self.swagger_types = {
            'ng_ap_cause': NgApCause,
            '_5g_mm_cause': Model5GMmCause,
            '_5g_sm_cause': Model5GSmCause
        }

        self.attribute_map = {
            'ng_ap_cause': 'ngApCause',
            '_5g_mm_cause': '5gMmCause',
            '_5g_sm_cause': '5gSmCause'
        }
        self._ng_ap_cause = ng_ap_cause
        self.__5g_mm_cause = _5g_mm_cause
        self.__5g_sm_cause = _5g_sm_cause

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RanNasRelCause of this RanNasRelCause.  # noqa: E501
        :rtype: RanNasRelCause
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ng_ap_cause(self):
        """Gets the ng_ap_cause of this RanNasRelCause.


        :return: The ng_ap_cause of this RanNasRelCause.
        :rtype: NgApCause
        """
        return self._ng_ap_cause

    @ng_ap_cause.setter
    def ng_ap_cause(self, ng_ap_cause):
        """Sets the ng_ap_cause of this RanNasRelCause.


        :param ng_ap_cause: The ng_ap_cause of this RanNasRelCause.
        :type ng_ap_cause: NgApCause
        """

        self._ng_ap_cause = ng_ap_cause

    @property
    def _5g_mm_cause(self):
        """Gets the _5g_mm_cause of this RanNasRelCause.


        :return: The _5g_mm_cause of this RanNasRelCause.
        :rtype: Model5GMmCause
        """
        return self.__5g_mm_cause

    @_5g_mm_cause.setter
    def _5g_mm_cause(self, _5g_mm_cause):
        """Sets the _5g_mm_cause of this RanNasRelCause.


        :param _5g_mm_cause: The _5g_mm_cause of this RanNasRelCause.
        :type _5g_mm_cause: Model5GMmCause
        """

        self.__5g_mm_cause = _5g_mm_cause

    @property
    def _5g_sm_cause(self):
        """Gets the _5g_sm_cause of this RanNasRelCause.


        :return: The _5g_sm_cause of this RanNasRelCause.
        :rtype: Model5GSmCause
        """
        return self.__5g_sm_cause

    @_5g_sm_cause.setter
    def _5g_sm_cause(self, _5g_sm_cause):
        """Sets the _5g_sm_cause of this RanNasRelCause.


        :param _5g_sm_cause: The _5g_sm_cause of this RanNasRelCause.
        :type _5g_sm_cause: Model5GSmCause
        """

        self.__5g_sm_cause = _5g_sm_cause
