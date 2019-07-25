# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.notification_cause import NotificationCause  # noqa: F401,E501
from swagger_server.models.qfi import Qfi  # noqa: F401,E501
from swagger_server import util


class QosFlowNotifyItem(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, qfi=None, notification_cause=None):  # noqa: E501
        """QosFlowNotifyItem - a model defined in Swagger

        :param qfi: The qfi of this QosFlowNotifyItem.  # noqa: E501
        :type qfi: Qfi
        :param notification_cause: The notification_cause of this QosFlowNotifyItem.  # noqa: E501
        :type notification_cause: NotificationCause
        """
        self.swagger_types = {
            'qfi': Qfi,
            'notification_cause': NotificationCause
        }

        self.attribute_map = {
            'qfi': 'qfi',
            'notification_cause': 'notificationCause'
        }
        self._qfi = qfi
        self._notification_cause = notification_cause

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The QosFlowNotifyItem of this QosFlowNotifyItem.  # noqa: E501
        :rtype: QosFlowNotifyItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def qfi(self):
        """Gets the qfi of this QosFlowNotifyItem.


        :return: The qfi of this QosFlowNotifyItem.
        :rtype: Qfi
        """
        return self._qfi

    @qfi.setter
    def qfi(self, qfi):
        """Sets the qfi of this QosFlowNotifyItem.


        :param qfi: The qfi of this QosFlowNotifyItem.
        :type qfi: Qfi
        """
        if qfi is None:
            raise ValueError("Invalid value for `qfi`, must not be `None`")  # noqa: E501

        self._qfi = qfi

    @property
    def notification_cause(self):
        """Gets the notification_cause of this QosFlowNotifyItem.


        :return: The notification_cause of this QosFlowNotifyItem.
        :rtype: NotificationCause
        """
        return self._notification_cause

    @notification_cause.setter
    def notification_cause(self, notification_cause):
        """Sets the notification_cause of this QosFlowNotifyItem.


        :param notification_cause: The notification_cause of this QosFlowNotifyItem.
        :type notification_cause: NotificationCause
        """
        if notification_cause is None:
            raise ValueError("Invalid value for `notification_cause`, must not be `None`")  # noqa: E501

        self._notification_cause = notification_cause
