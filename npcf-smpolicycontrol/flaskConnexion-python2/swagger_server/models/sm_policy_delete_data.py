# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.accu_usage_report import AccuUsageReport  # noqa: F401,E501
from swagger_server.models.network_id import NetworkId  # noqa: F401,E501
from swagger_server.models.ran_nas_rel_cause import RanNasRelCause  # noqa: F401,E501
from swagger_server.models.time_zone import TimeZone  # noqa: F401,E501
from swagger_server.models.user_location import UserLocation  # noqa: F401,E501
from swagger_server import util


class SmPolicyDeleteData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, user_location_info=None, ue_time_zone=None, serving_network=None, user_location_info_time=None, ran_nas_rel_causes=None, accu_usage_reports=None):  # noqa: E501
        """SmPolicyDeleteData - a model defined in Swagger

        :param user_location_info: The user_location_info of this SmPolicyDeleteData.  # noqa: E501
        :type user_location_info: UserLocation
        :param ue_time_zone: The ue_time_zone of this SmPolicyDeleteData.  # noqa: E501
        :type ue_time_zone: TimeZone
        :param serving_network: The serving_network of this SmPolicyDeleteData.  # noqa: E501
        :type serving_network: NetworkId
        :param user_location_info_time: The user_location_info_time of this SmPolicyDeleteData.  # noqa: E501
        :type user_location_info_time: datetime
        :param ran_nas_rel_causes: The ran_nas_rel_causes of this SmPolicyDeleteData.  # noqa: E501
        :type ran_nas_rel_causes: List[RanNasRelCause]
        :param accu_usage_reports: The accu_usage_reports of this SmPolicyDeleteData.  # noqa: E501
        :type accu_usage_reports: List[AccuUsageReport]
        """
        self.swagger_types = {
            'user_location_info': UserLocation,
            'ue_time_zone': TimeZone,
            'serving_network': NetworkId,
            'user_location_info_time': datetime,
            'ran_nas_rel_causes': List[RanNasRelCause],
            'accu_usage_reports': List[AccuUsageReport]
        }

        self.attribute_map = {
            'user_location_info': 'userLocationInfo',
            'ue_time_zone': 'ueTimeZone',
            'serving_network': 'servingNetwork',
            'user_location_info_time': 'userLocationInfoTime',
            'ran_nas_rel_causes': 'ranNasRelCauses',
            'accu_usage_reports': 'accuUsageReports'
        }
        self._user_location_info = user_location_info
        self._ue_time_zone = ue_time_zone
        self._serving_network = serving_network
        self._user_location_info_time = user_location_info_time
        self._ran_nas_rel_causes = ran_nas_rel_causes
        self._accu_usage_reports = accu_usage_reports

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SmPolicyDeleteData of this SmPolicyDeleteData.  # noqa: E501
        :rtype: SmPolicyDeleteData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_location_info(self):
        """Gets the user_location_info of this SmPolicyDeleteData.


        :return: The user_location_info of this SmPolicyDeleteData.
        :rtype: UserLocation
        """
        return self._user_location_info

    @user_location_info.setter
    def user_location_info(self, user_location_info):
        """Sets the user_location_info of this SmPolicyDeleteData.


        :param user_location_info: The user_location_info of this SmPolicyDeleteData.
        :type user_location_info: UserLocation
        """

        self._user_location_info = user_location_info

    @property
    def ue_time_zone(self):
        """Gets the ue_time_zone of this SmPolicyDeleteData.


        :return: The ue_time_zone of this SmPolicyDeleteData.
        :rtype: TimeZone
        """
        return self._ue_time_zone

    @ue_time_zone.setter
    def ue_time_zone(self, ue_time_zone):
        """Sets the ue_time_zone of this SmPolicyDeleteData.


        :param ue_time_zone: The ue_time_zone of this SmPolicyDeleteData.
        :type ue_time_zone: TimeZone
        """

        self._ue_time_zone = ue_time_zone

    @property
    def serving_network(self):
        """Gets the serving_network of this SmPolicyDeleteData.


        :return: The serving_network of this SmPolicyDeleteData.
        :rtype: NetworkId
        """
        return self._serving_network

    @serving_network.setter
    def serving_network(self, serving_network):
        """Sets the serving_network of this SmPolicyDeleteData.


        :param serving_network: The serving_network of this SmPolicyDeleteData.
        :type serving_network: NetworkId
        """

        self._serving_network = serving_network

    @property
    def user_location_info_time(self):
        """Gets the user_location_info_time of this SmPolicyDeleteData.


        :return: The user_location_info_time of this SmPolicyDeleteData.
        :rtype: datetime
        """
        return self._user_location_info_time

    @user_location_info_time.setter
    def user_location_info_time(self, user_location_info_time):
        """Sets the user_location_info_time of this SmPolicyDeleteData.


        :param user_location_info_time: The user_location_info_time of this SmPolicyDeleteData.
        :type user_location_info_time: datetime
        """

        self._user_location_info_time = user_location_info_time

    @property
    def ran_nas_rel_causes(self):
        """Gets the ran_nas_rel_causes of this SmPolicyDeleteData.

        Contains the RAN and/or NAS release cause.  # noqa: E501

        :return: The ran_nas_rel_causes of this SmPolicyDeleteData.
        :rtype: List[RanNasRelCause]
        """
        return self._ran_nas_rel_causes

    @ran_nas_rel_causes.setter
    def ran_nas_rel_causes(self, ran_nas_rel_causes):
        """Sets the ran_nas_rel_causes of this SmPolicyDeleteData.

        Contains the RAN and/or NAS release cause.  # noqa: E501

        :param ran_nas_rel_causes: The ran_nas_rel_causes of this SmPolicyDeleteData.
        :type ran_nas_rel_causes: List[RanNasRelCause]
        """

        self._ran_nas_rel_causes = ran_nas_rel_causes

    @property
    def accu_usage_reports(self):
        """Gets the accu_usage_reports of this SmPolicyDeleteData.

        Contains the usage report  # noqa: E501

        :return: The accu_usage_reports of this SmPolicyDeleteData.
        :rtype: List[AccuUsageReport]
        """
        return self._accu_usage_reports

    @accu_usage_reports.setter
    def accu_usage_reports(self, accu_usage_reports):
        """Sets the accu_usage_reports of this SmPolicyDeleteData.

        Contains the usage report  # noqa: E501

        :param accu_usage_reports: The accu_usage_reports of this SmPolicyDeleteData.
        :type accu_usage_reports: List[AccuUsageReport]
        """

        self._accu_usage_reports = accu_usage_reports
