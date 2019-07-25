# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.ipv4_addr import Ipv4Addr  # noqa: F401,E501
from swagger_server.models.ipv6_addr import Ipv6Addr  # noqa: F401,E501
from swagger_server.models.uinteger import Uinteger  # noqa: F401,E501
from swagger_server import util


class RouteInformation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ipv4_addr=None, ipv6_addr=None, port_number=None):  # noqa: E501
        """RouteInformation - a model defined in Swagger

        :param ipv4_addr: The ipv4_addr of this RouteInformation.  # noqa: E501
        :type ipv4_addr: Ipv4Addr
        :param ipv6_addr: The ipv6_addr of this RouteInformation.  # noqa: E501
        :type ipv6_addr: Ipv6Addr
        :param port_number: The port_number of this RouteInformation.  # noqa: E501
        :type port_number: Uinteger
        """
        self.swagger_types = {
            'ipv4_addr': Ipv4Addr,
            'ipv6_addr': Ipv6Addr,
            'port_number': Uinteger
        }

        self.attribute_map = {
            'ipv4_addr': 'ipv4Addr',
            'ipv6_addr': 'ipv6Addr',
            'port_number': 'portNumber'
        }
        self._ipv4_addr = ipv4_addr
        self._ipv6_addr = ipv6_addr
        self._port_number = port_number

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RouteInformation of this RouteInformation.  # noqa: E501
        :rtype: RouteInformation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ipv4_addr(self):
        """Gets the ipv4_addr of this RouteInformation.


        :return: The ipv4_addr of this RouteInformation.
        :rtype: Ipv4Addr
        """
        return self._ipv4_addr

    @ipv4_addr.setter
    def ipv4_addr(self, ipv4_addr):
        """Sets the ipv4_addr of this RouteInformation.


        :param ipv4_addr: The ipv4_addr of this RouteInformation.
        :type ipv4_addr: Ipv4Addr
        """

        self._ipv4_addr = ipv4_addr

    @property
    def ipv6_addr(self):
        """Gets the ipv6_addr of this RouteInformation.


        :return: The ipv6_addr of this RouteInformation.
        :rtype: Ipv6Addr
        """
        return self._ipv6_addr

    @ipv6_addr.setter
    def ipv6_addr(self, ipv6_addr):
        """Sets the ipv6_addr of this RouteInformation.


        :param ipv6_addr: The ipv6_addr of this RouteInformation.
        :type ipv6_addr: Ipv6Addr
        """

        self._ipv6_addr = ipv6_addr

    @property
    def port_number(self):
        """Gets the port_number of this RouteInformation.


        :return: The port_number of this RouteInformation.
        :rtype: Uinteger
        """
        return self._port_number

    @port_number.setter
    def port_number(self, port_number):
        """Sets the port_number of this RouteInformation.


        :param port_number: The port_number of this RouteInformation.
        :type port_number: Uinteger
        """
        if port_number is None:
            raise ValueError("Invalid value for `port_number`, must not be `None`")  # noqa: E501

        self._port_number = port_number
