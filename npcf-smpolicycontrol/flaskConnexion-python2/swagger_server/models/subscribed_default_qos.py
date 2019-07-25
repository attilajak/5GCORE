# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.arp import Arp  # noqa: F401,E501
from swagger_server.models.model5_qi import Model5Qi  # noqa: F401,E501
from swagger_server.models.model5_qi_priority_level import Model5QiPriorityLevel  # noqa: F401,E501
from swagger_server import util


class SubscribedDefaultQos(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, _5qi=None, arp=None, priority_level=None):  # noqa: E501
        """SubscribedDefaultQos - a model defined in Swagger

        :param _5qi: The _5qi of this SubscribedDefaultQos.  # noqa: E501
        :type _5qi: Model5Qi
        :param arp: The arp of this SubscribedDefaultQos.  # noqa: E501
        :type arp: Arp
        :param priority_level: The priority_level of this SubscribedDefaultQos.  # noqa: E501
        :type priority_level: Model5QiPriorityLevel
        """
        self.swagger_types = {
            '_5qi': Model5Qi,
            'arp': Arp,
            'priority_level': Model5QiPriorityLevel
        }

        self.attribute_map = {
            '_5qi': '5qi',
            'arp': 'arp',
            'priority_level': 'priorityLevel'
        }
        self.__5qi = _5qi
        self._arp = arp
        self._priority_level = priority_level

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubscribedDefaultQos of this SubscribedDefaultQos.  # noqa: E501
        :rtype: SubscribedDefaultQos
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _5qi(self):
        """Gets the _5qi of this SubscribedDefaultQos.


        :return: The _5qi of this SubscribedDefaultQos.
        :rtype: Model5Qi
        """
        return self.__5qi

    @_5qi.setter
    def _5qi(self, _5qi):
        """Sets the _5qi of this SubscribedDefaultQos.


        :param _5qi: The _5qi of this SubscribedDefaultQos.
        :type _5qi: Model5Qi
        """
        if _5qi is None:
            raise ValueError("Invalid value for `_5qi`, must not be `None`")  # noqa: E501

        self.__5qi = _5qi

    @property
    def arp(self):
        """Gets the arp of this SubscribedDefaultQos.


        :return: The arp of this SubscribedDefaultQos.
        :rtype: Arp
        """
        return self._arp

    @arp.setter
    def arp(self, arp):
        """Sets the arp of this SubscribedDefaultQos.


        :param arp: The arp of this SubscribedDefaultQos.
        :type arp: Arp
        """
        if arp is None:
            raise ValueError("Invalid value for `arp`, must not be `None`")  # noqa: E501

        self._arp = arp

    @property
    def priority_level(self):
        """Gets the priority_level of this SubscribedDefaultQos.


        :return: The priority_level of this SubscribedDefaultQos.
        :rtype: Model5QiPriorityLevel
        """
        return self._priority_level

    @priority_level.setter
    def priority_level(self, priority_level):
        """Sets the priority_level of this SubscribedDefaultQos.


        :param priority_level: The priority_level of this SubscribedDefaultQos.
        :type priority_level: Model5QiPriorityLevel
        """

        self._priority_level = priority_level
