# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.ipv4_addr import Ipv4Addr  # noqa: F401,E501
from swagger_server.models.ipv6_addr import Ipv6Addr  # noqa: F401,E501
from swagger_server.models.teid import Teid  # noqa: F401,E501
from swagger_server import util


class TunnelInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ipv4_addr=None, ipv6_addr=None, gtp_teid=None):  # noqa: E501
        """TunnelInfo - a model defined in Swagger

        :param ipv4_addr: The ipv4_addr of this TunnelInfo.  # noqa: E501
        :type ipv4_addr: Ipv4Addr
        :param ipv6_addr: The ipv6_addr of this TunnelInfo.  # noqa: E501
        :type ipv6_addr: Ipv6Addr
        :param gtp_teid: The gtp_teid of this TunnelInfo.  # noqa: E501
        :type gtp_teid: Teid
        """
        self.swagger_types = {
            'ipv4_addr': Ipv4Addr,
            'ipv6_addr': Ipv6Addr,
            'gtp_teid': Teid
        }

        self.attribute_map = {
            'ipv4_addr': 'ipv4Addr',
            'ipv6_addr': 'ipv6Addr',
            'gtp_teid': 'gtpTeid'
        }
        self._ipv4_addr = ipv4_addr
        self._ipv6_addr = ipv6_addr
        self._gtp_teid = gtp_teid

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TunnelInfo of this TunnelInfo.  # noqa: E501
        :rtype: TunnelInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ipv4_addr(self):
        """Gets the ipv4_addr of this TunnelInfo.


        :return: The ipv4_addr of this TunnelInfo.
        :rtype: Ipv4Addr
        """
        return self._ipv4_addr

    @ipv4_addr.setter
    def ipv4_addr(self, ipv4_addr):
        """Sets the ipv4_addr of this TunnelInfo.


        :param ipv4_addr: The ipv4_addr of this TunnelInfo.
        :type ipv4_addr: Ipv4Addr
        """

        self._ipv4_addr = ipv4_addr

    @property
    def ipv6_addr(self):
        """Gets the ipv6_addr of this TunnelInfo.


        :return: The ipv6_addr of this TunnelInfo.
        :rtype: Ipv6Addr
        """
        return self._ipv6_addr

    @ipv6_addr.setter
    def ipv6_addr(self, ipv6_addr):
        """Sets the ipv6_addr of this TunnelInfo.


        :param ipv6_addr: The ipv6_addr of this TunnelInfo.
        :type ipv6_addr: Ipv6Addr
        """

        self._ipv6_addr = ipv6_addr

    @property
    def gtp_teid(self):
        """Gets the gtp_teid of this TunnelInfo.


        :return: The gtp_teid of this TunnelInfo.
        :rtype: Teid
        """
        return self._gtp_teid

    @gtp_teid.setter
    def gtp_teid(self, gtp_teid):
        """Sets the gtp_teid of this TunnelInfo.


        :param gtp_teid: The gtp_teid of this TunnelInfo.
        :type gtp_teid: Teid
        """
        if gtp_teid is None:
            raise ValueError("Invalid value for `gtp_teid`, must not be `None`")  # noqa: E501

        self._gtp_teid = gtp_teid
