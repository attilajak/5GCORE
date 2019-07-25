# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.duration_sec import DurationSec  # noqa: F401,E501
from swagger_server.models.trigger_category import TriggerCategory  # noqa: F401,E501
from swagger_server.models.trigger_type import TriggerType  # noqa: F401,E501
from swagger_server.models.uint32 import Uint32  # noqa: F401,E501
from swagger_server.models.uint64 import Uint64  # noqa: F401,E501
from swagger_server import util


class Trigger(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, trigger_type=None, trigger_category=None, time_limit=None, volume_limit=None, volume_limit64=None, max_number_ofccc=None):  # noqa: E501
        """Trigger - a model defined in Swagger

        :param trigger_type: The trigger_type of this Trigger.  # noqa: E501
        :type trigger_type: TriggerType
        :param trigger_category: The trigger_category of this Trigger.  # noqa: E501
        :type trigger_category: TriggerCategory
        :param time_limit: The time_limit of this Trigger.  # noqa: E501
        :type time_limit: DurationSec
        :param volume_limit: The volume_limit of this Trigger.  # noqa: E501
        :type volume_limit: Uint32
        :param volume_limit64: The volume_limit64 of this Trigger.  # noqa: E501
        :type volume_limit64: Uint64
        :param max_number_ofccc: The max_number_ofccc of this Trigger.  # noqa: E501
        :type max_number_ofccc: Uint32
        """
        self.swagger_types = {
            'trigger_type': TriggerType,
            'trigger_category': TriggerCategory,
            'time_limit': DurationSec,
            'volume_limit': Uint32,
            'volume_limit64': Uint64,
            'max_number_ofccc': Uint32
        }

        self.attribute_map = {
            'trigger_type': 'triggerType',
            'trigger_category': 'triggerCategory',
            'time_limit': 'timeLimit',
            'volume_limit': 'volumeLimit',
            'volume_limit64': 'volumeLimit64',
            'max_number_ofccc': 'maxNumberOfccc'
        }
        self._trigger_type = trigger_type
        self._trigger_category = trigger_category
        self._time_limit = time_limit
        self._volume_limit = volume_limit
        self._volume_limit64 = volume_limit64
        self._max_number_ofccc = max_number_ofccc

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Trigger of this Trigger.  # noqa: E501
        :rtype: Trigger
        """
        return util.deserialize_model(dikt, cls)

    @property
    def trigger_type(self):
        """Gets the trigger_type of this Trigger.


        :return: The trigger_type of this Trigger.
        :rtype: TriggerType
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this Trigger.


        :param trigger_type: The trigger_type of this Trigger.
        :type trigger_type: TriggerType
        """
        if trigger_type is None:
            raise ValueError("Invalid value for `trigger_type`, must not be `None`")  # noqa: E501

        self._trigger_type = trigger_type

    @property
    def trigger_category(self):
        """Gets the trigger_category of this Trigger.


        :return: The trigger_category of this Trigger.
        :rtype: TriggerCategory
        """
        return self._trigger_category

    @trigger_category.setter
    def trigger_category(self, trigger_category):
        """Sets the trigger_category of this Trigger.


        :param trigger_category: The trigger_category of this Trigger.
        :type trigger_category: TriggerCategory
        """
        if trigger_category is None:
            raise ValueError("Invalid value for `trigger_category`, must not be `None`")  # noqa: E501

        self._trigger_category = trigger_category

    @property
    def time_limit(self):
        """Gets the time_limit of this Trigger.


        :return: The time_limit of this Trigger.
        :rtype: DurationSec
        """
        return self._time_limit

    @time_limit.setter
    def time_limit(self, time_limit):
        """Sets the time_limit of this Trigger.


        :param time_limit: The time_limit of this Trigger.
        :type time_limit: DurationSec
        """

        self._time_limit = time_limit

    @property
    def volume_limit(self):
        """Gets the volume_limit of this Trigger.


        :return: The volume_limit of this Trigger.
        :rtype: Uint32
        """
        return self._volume_limit

    @volume_limit.setter
    def volume_limit(self, volume_limit):
        """Sets the volume_limit of this Trigger.


        :param volume_limit: The volume_limit of this Trigger.
        :type volume_limit: Uint32
        """

        self._volume_limit = volume_limit

    @property
    def volume_limit64(self):
        """Gets the volume_limit64 of this Trigger.


        :return: The volume_limit64 of this Trigger.
        :rtype: Uint64
        """
        return self._volume_limit64

    @volume_limit64.setter
    def volume_limit64(self, volume_limit64):
        """Sets the volume_limit64 of this Trigger.


        :param volume_limit64: The volume_limit64 of this Trigger.
        :type volume_limit64: Uint64
        """

        self._volume_limit64 = volume_limit64

    @property
    def max_number_ofccc(self):
        """Gets the max_number_ofccc of this Trigger.


        :return: The max_number_ofccc of this Trigger.
        :rtype: Uint32
        """
        return self._max_number_ofccc

    @max_number_ofccc.setter
    def max_number_ofccc(self, max_number_ofccc):
        """Sets the max_number_ofccc of this Trigger.


        :param max_number_ofccc: The max_number_ofccc of this Trigger.
        :type max_number_ofccc: Uint32
        """

        self._max_number_ofccc = max_number_ofccc
