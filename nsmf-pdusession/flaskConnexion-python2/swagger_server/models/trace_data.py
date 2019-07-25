# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.ipv4_addr import Ipv4Addr  # noqa: F401,E501
from swagger_server.models.ipv6_addr import Ipv6Addr  # noqa: F401,E501
from swagger_server.models.trace_depth import TraceDepth  # noqa: F401,E501
import re  # noqa: F401,E501
from swagger_server import util


class TraceData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, trace_ref=None, trace_depth=None, ne_type_list=None, event_list=None, collection_entity_ipv4_addr=None, collection_entity_ipv6_addr=None, interface_list=None):  # noqa: E501
        """TraceData - a model defined in Swagger

        :param trace_ref: The trace_ref of this TraceData.  # noqa: E501
        :type trace_ref: str
        :param trace_depth: The trace_depth of this TraceData.  # noqa: E501
        :type trace_depth: TraceDepth
        :param ne_type_list: The ne_type_list of this TraceData.  # noqa: E501
        :type ne_type_list: str
        :param event_list: The event_list of this TraceData.  # noqa: E501
        :type event_list: str
        :param collection_entity_ipv4_addr: The collection_entity_ipv4_addr of this TraceData.  # noqa: E501
        :type collection_entity_ipv4_addr: Ipv4Addr
        :param collection_entity_ipv6_addr: The collection_entity_ipv6_addr of this TraceData.  # noqa: E501
        :type collection_entity_ipv6_addr: Ipv6Addr
        :param interface_list: The interface_list of this TraceData.  # noqa: E501
        :type interface_list: str
        """
        self.swagger_types = {
            'trace_ref': str,
            'trace_depth': TraceDepth,
            'ne_type_list': str,
            'event_list': str,
            'collection_entity_ipv4_addr': Ipv4Addr,
            'collection_entity_ipv6_addr': Ipv6Addr,
            'interface_list': str
        }

        self.attribute_map = {
            'trace_ref': 'traceRef',
            'trace_depth': 'traceDepth',
            'ne_type_list': 'neTypeList',
            'event_list': 'eventList',
            'collection_entity_ipv4_addr': 'collectionEntityIpv4Addr',
            'collection_entity_ipv6_addr': 'collectionEntityIpv6Addr',
            'interface_list': 'interfaceList'
        }
        self._trace_ref = trace_ref
        self._trace_depth = trace_depth
        self._ne_type_list = ne_type_list
        self._event_list = event_list
        self._collection_entity_ipv4_addr = collection_entity_ipv4_addr
        self._collection_entity_ipv6_addr = collection_entity_ipv6_addr
        self._interface_list = interface_list

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TraceData of this TraceData.  # noqa: E501
        :rtype: TraceData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def trace_ref(self):
        """Gets the trace_ref of this TraceData.


        :return: The trace_ref of this TraceData.
        :rtype: str
        """
        return self._trace_ref

    @trace_ref.setter
    def trace_ref(self, trace_ref):
        """Sets the trace_ref of this TraceData.


        :param trace_ref: The trace_ref of this TraceData.
        :type trace_ref: str
        """
        if trace_ref is None:
            raise ValueError("Invalid value for `trace_ref`, must not be `None`")  # noqa: E501

        self._trace_ref = trace_ref

    @property
    def trace_depth(self):
        """Gets the trace_depth of this TraceData.


        :return: The trace_depth of this TraceData.
        :rtype: TraceDepth
        """
        return self._trace_depth

    @trace_depth.setter
    def trace_depth(self, trace_depth):
        """Sets the trace_depth of this TraceData.


        :param trace_depth: The trace_depth of this TraceData.
        :type trace_depth: TraceDepth
        """
        if trace_depth is None:
            raise ValueError("Invalid value for `trace_depth`, must not be `None`")  # noqa: E501

        self._trace_depth = trace_depth

    @property
    def ne_type_list(self):
        """Gets the ne_type_list of this TraceData.


        :return: The ne_type_list of this TraceData.
        :rtype: str
        """
        return self._ne_type_list

    @ne_type_list.setter
    def ne_type_list(self, ne_type_list):
        """Sets the ne_type_list of this TraceData.


        :param ne_type_list: The ne_type_list of this TraceData.
        :type ne_type_list: str
        """
        if ne_type_list is None:
            raise ValueError("Invalid value for `ne_type_list`, must not be `None`")  # noqa: E501

        self._ne_type_list = ne_type_list

    @property
    def event_list(self):
        """Gets the event_list of this TraceData.


        :return: The event_list of this TraceData.
        :rtype: str
        """
        return self._event_list

    @event_list.setter
    def event_list(self, event_list):
        """Sets the event_list of this TraceData.


        :param event_list: The event_list of this TraceData.
        :type event_list: str
        """
        if event_list is None:
            raise ValueError("Invalid value for `event_list`, must not be `None`")  # noqa: E501

        self._event_list = event_list

    @property
    def collection_entity_ipv4_addr(self):
        """Gets the collection_entity_ipv4_addr of this TraceData.


        :return: The collection_entity_ipv4_addr of this TraceData.
        :rtype: Ipv4Addr
        """
        return self._collection_entity_ipv4_addr

    @collection_entity_ipv4_addr.setter
    def collection_entity_ipv4_addr(self, collection_entity_ipv4_addr):
        """Sets the collection_entity_ipv4_addr of this TraceData.


        :param collection_entity_ipv4_addr: The collection_entity_ipv4_addr of this TraceData.
        :type collection_entity_ipv4_addr: Ipv4Addr
        """

        self._collection_entity_ipv4_addr = collection_entity_ipv4_addr

    @property
    def collection_entity_ipv6_addr(self):
        """Gets the collection_entity_ipv6_addr of this TraceData.


        :return: The collection_entity_ipv6_addr of this TraceData.
        :rtype: Ipv6Addr
        """
        return self._collection_entity_ipv6_addr

    @collection_entity_ipv6_addr.setter
    def collection_entity_ipv6_addr(self, collection_entity_ipv6_addr):
        """Sets the collection_entity_ipv6_addr of this TraceData.


        :param collection_entity_ipv6_addr: The collection_entity_ipv6_addr of this TraceData.
        :type collection_entity_ipv6_addr: Ipv6Addr
        """

        self._collection_entity_ipv6_addr = collection_entity_ipv6_addr

    @property
    def interface_list(self):
        """Gets the interface_list of this TraceData.


        :return: The interface_list of this TraceData.
        :rtype: str
        """
        return self._interface_list

    @interface_list.setter
    def interface_list(self, interface_list):
        """Sets the interface_list of this TraceData.


        :param interface_list: The interface_list of this TraceData.
        :type interface_list: str
        """

        self._interface_list = interface_list
