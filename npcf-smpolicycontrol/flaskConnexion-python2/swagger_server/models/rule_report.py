# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.content_version import ContentVersion  # noqa: F401,E501
from swagger_server.models.failure_code import FailureCode  # noqa: F401,E501
from swagger_server.models.final_unit_action import FinalUnitAction  # noqa: F401,E501
from swagger_server.models.ran_nas_rel_cause import RanNasRelCause  # noqa: F401,E501
from swagger_server.models.rule_status import RuleStatus  # noqa: F401,E501
from swagger_server import util


class RuleReport(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, pcc_rule_ids=None, rule_status=None, cont_vers=None, failure_code=None, fin_unit_act=None, ran_nas_rel_causes=None):  # noqa: E501
        """RuleReport - a model defined in Swagger

        :param pcc_rule_ids: The pcc_rule_ids of this RuleReport.  # noqa: E501
        :type pcc_rule_ids: List[str]
        :param rule_status: The rule_status of this RuleReport.  # noqa: E501
        :type rule_status: RuleStatus
        :param cont_vers: The cont_vers of this RuleReport.  # noqa: E501
        :type cont_vers: List[ContentVersion]
        :param failure_code: The failure_code of this RuleReport.  # noqa: E501
        :type failure_code: FailureCode
        :param fin_unit_act: The fin_unit_act of this RuleReport.  # noqa: E501
        :type fin_unit_act: FinalUnitAction
        :param ran_nas_rel_causes: The ran_nas_rel_causes of this RuleReport.  # noqa: E501
        :type ran_nas_rel_causes: List[RanNasRelCause]
        """
        self.swagger_types = {
            'pcc_rule_ids': List[str],
            'rule_status': RuleStatus,
            'cont_vers': List[ContentVersion],
            'failure_code': FailureCode,
            'fin_unit_act': FinalUnitAction,
            'ran_nas_rel_causes': List[RanNasRelCause]
        }

        self.attribute_map = {
            'pcc_rule_ids': 'pccRuleIds',
            'rule_status': 'ruleStatus',
            'cont_vers': 'contVers',
            'failure_code': 'failureCode',
            'fin_unit_act': 'finUnitAct',
            'ran_nas_rel_causes': 'ranNasRelCauses'
        }
        self._pcc_rule_ids = pcc_rule_ids
        self._rule_status = rule_status
        self._cont_vers = cont_vers
        self._failure_code = failure_code
        self._fin_unit_act = fin_unit_act
        self._ran_nas_rel_causes = ran_nas_rel_causes

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RuleReport of this RuleReport.  # noqa: E501
        :rtype: RuleReport
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pcc_rule_ids(self):
        """Gets the pcc_rule_ids of this RuleReport.

        Contains the identifier of the affected PCC rule(s).  # noqa: E501

        :return: The pcc_rule_ids of this RuleReport.
        :rtype: List[str]
        """
        return self._pcc_rule_ids

    @pcc_rule_ids.setter
    def pcc_rule_ids(self, pcc_rule_ids):
        """Sets the pcc_rule_ids of this RuleReport.

        Contains the identifier of the affected PCC rule(s).  # noqa: E501

        :param pcc_rule_ids: The pcc_rule_ids of this RuleReport.
        :type pcc_rule_ids: List[str]
        """
        if pcc_rule_ids is None:
            raise ValueError("Invalid value for `pcc_rule_ids`, must not be `None`")  # noqa: E501

        self._pcc_rule_ids = pcc_rule_ids

    @property
    def rule_status(self):
        """Gets the rule_status of this RuleReport.


        :return: The rule_status of this RuleReport.
        :rtype: RuleStatus
        """
        return self._rule_status

    @rule_status.setter
    def rule_status(self, rule_status):
        """Sets the rule_status of this RuleReport.


        :param rule_status: The rule_status of this RuleReport.
        :type rule_status: RuleStatus
        """
        if rule_status is None:
            raise ValueError("Invalid value for `rule_status`, must not be `None`")  # noqa: E501

        self._rule_status = rule_status

    @property
    def cont_vers(self):
        """Gets the cont_vers of this RuleReport.

        Indicates the version of a PCC rule.  # noqa: E501

        :return: The cont_vers of this RuleReport.
        :rtype: List[ContentVersion]
        """
        return self._cont_vers

    @cont_vers.setter
    def cont_vers(self, cont_vers):
        """Sets the cont_vers of this RuleReport.

        Indicates the version of a PCC rule.  # noqa: E501

        :param cont_vers: The cont_vers of this RuleReport.
        :type cont_vers: List[ContentVersion]
        """

        self._cont_vers = cont_vers

    @property
    def failure_code(self):
        """Gets the failure_code of this RuleReport.


        :return: The failure_code of this RuleReport.
        :rtype: FailureCode
        """
        return self._failure_code

    @failure_code.setter
    def failure_code(self, failure_code):
        """Sets the failure_code of this RuleReport.


        :param failure_code: The failure_code of this RuleReport.
        :type failure_code: FailureCode
        """

        self._failure_code = failure_code

    @property
    def fin_unit_act(self):
        """Gets the fin_unit_act of this RuleReport.


        :return: The fin_unit_act of this RuleReport.
        :rtype: FinalUnitAction
        """
        return self._fin_unit_act

    @fin_unit_act.setter
    def fin_unit_act(self, fin_unit_act):
        """Sets the fin_unit_act of this RuleReport.


        :param fin_unit_act: The fin_unit_act of this RuleReport.
        :type fin_unit_act: FinalUnitAction
        """

        self._fin_unit_act = fin_unit_act

    @property
    def ran_nas_rel_causes(self):
        """Gets the ran_nas_rel_causes of this RuleReport.

        indicates the RAN or NAS release cause code information.  # noqa: E501

        :return: The ran_nas_rel_causes of this RuleReport.
        :rtype: List[RanNasRelCause]
        """
        return self._ran_nas_rel_causes

    @ran_nas_rel_causes.setter
    def ran_nas_rel_causes(self, ran_nas_rel_causes):
        """Sets the ran_nas_rel_causes of this RuleReport.

        indicates the RAN or NAS release cause code information.  # noqa: E501

        :param ran_nas_rel_causes: The ran_nas_rel_causes of this RuleReport.
        :type ran_nas_rel_causes: List[RanNasRelCause]
        """

        self._ran_nas_rel_causes = ran_nas_rel_causes