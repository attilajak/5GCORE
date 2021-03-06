# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.access_type import AccessType  # noqa: F401,E501
from swagger_server.models.backup_amf_info import BackupAmfInfo  # noqa: F401,E501
from swagger_server.models.cause import Cause  # noqa: F401,E501
from swagger_server.models.eps_bearer_container import EpsBearerContainer  # noqa: F401,E501
from swagger_server.models.eps_bearer_id import EpsBearerId  # noqa: F401,E501
from swagger_server.models.eps_interworking_indication import EpsInterworkingIndication  # noqa: F401,E501
from swagger_server.models.guami import Guami  # noqa: F401,E501
from swagger_server.models.ho_state import HoState  # noqa: F401,E501
from swagger_server.models.model5_g_mm_cause import Model5GMmCause  # noqa: F401,E501
from swagger_server.models.n2_sm_info_type import N2SmInfoType  # noqa: F401,E501
from swagger_server.models.nf_instance_id import NfInstanceId  # noqa: F401,E501
from swagger_server.models.ng_ap_cause import NgApCause  # noqa: F401,E501
from swagger_server.models.ng_ran_target_id import NgRanTargetId  # noqa: F401,E501
from swagger_server.models.pei import Pei  # noqa: F401,E501
from swagger_server.models.plmn_id import PlmnId  # noqa: F401,E501
from swagger_server.models.presence_state import PresenceState  # noqa: F401,E501
from swagger_server.models.rat_type import RatType  # noqa: F401,E501
from swagger_server.models.ref_to_binary_data import RefToBinaryData  # noqa: F401,E501
from swagger_server.models.snssai import Snssai  # noqa: F401,E501
from swagger_server.models.time_zone import TimeZone  # noqa: F401,E501
from swagger_server.models.trace_data import TraceData  # noqa: F401,E501
from swagger_server.models.up_cnx_state import UpCnxState  # noqa: F401,E501
from swagger_server.models.uri import Uri  # noqa: F401,E501
from swagger_server.models.user_location import UserLocation  # noqa: F401,E501
from swagger_server import util


class SmContextUpdateData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, pei=None, serving_nf_id=None, guami=None, serving_network=None, backup_amf_info=None, an_type=None, rat_type=None, presence_in_ladn=None, ue_location=None, ue_time_zone=None, add_ue_location=None, up_cnx_state=None, ho_state=None, to_be_switched=False, failed_to_be_switched=None, n1_sm_msg=None, n2_sm_info=None, n2_sm_info_type=None, target_id=None, target_serving_nf_id=None, sm_context_status_uri=None, data_forwarding=False, eps_bearer_setup=None, revoke_ebi_list=None, release=False, cause=None, ng_ap_cause=None, _5g_mm_cause_value=None, s_nssai=None, trace_data=None, eps_interworking_ind=None, an_type_can_be_changed=False, n2_sm_info_ext1=None, n2_sm_info_type_ext1=None):  # noqa: E501
        """SmContextUpdateData - a model defined in Swagger

        :param pei: The pei of this SmContextUpdateData.  # noqa: E501
        :type pei: Pei
        :param serving_nf_id: The serving_nf_id of this SmContextUpdateData.  # noqa: E501
        :type serving_nf_id: NfInstanceId
        :param guami: The guami of this SmContextUpdateData.  # noqa: E501
        :type guami: Guami
        :param serving_network: The serving_network of this SmContextUpdateData.  # noqa: E501
        :type serving_network: PlmnId
        :param backup_amf_info: The backup_amf_info of this SmContextUpdateData.  # noqa: E501
        :type backup_amf_info: List[BackupAmfInfo]
        :param an_type: The an_type of this SmContextUpdateData.  # noqa: E501
        :type an_type: AccessType
        :param rat_type: The rat_type of this SmContextUpdateData.  # noqa: E501
        :type rat_type: RatType
        :param presence_in_ladn: The presence_in_ladn of this SmContextUpdateData.  # noqa: E501
        :type presence_in_ladn: PresenceState
        :param ue_location: The ue_location of this SmContextUpdateData.  # noqa: E501
        :type ue_location: UserLocation
        :param ue_time_zone: The ue_time_zone of this SmContextUpdateData.  # noqa: E501
        :type ue_time_zone: TimeZone
        :param add_ue_location: The add_ue_location of this SmContextUpdateData.  # noqa: E501
        :type add_ue_location: UserLocation
        :param up_cnx_state: The up_cnx_state of this SmContextUpdateData.  # noqa: E501
        :type up_cnx_state: UpCnxState
        :param ho_state: The ho_state of this SmContextUpdateData.  # noqa: E501
        :type ho_state: HoState
        :param to_be_switched: The to_be_switched of this SmContextUpdateData.  # noqa: E501
        :type to_be_switched: bool
        :param failed_to_be_switched: The failed_to_be_switched of this SmContextUpdateData.  # noqa: E501
        :type failed_to_be_switched: bool
        :param n1_sm_msg: The n1_sm_msg of this SmContextUpdateData.  # noqa: E501
        :type n1_sm_msg: RefToBinaryData
        :param n2_sm_info: The n2_sm_info of this SmContextUpdateData.  # noqa: E501
        :type n2_sm_info: RefToBinaryData
        :param n2_sm_info_type: The n2_sm_info_type of this SmContextUpdateData.  # noqa: E501
        :type n2_sm_info_type: N2SmInfoType
        :param target_id: The target_id of this SmContextUpdateData.  # noqa: E501
        :type target_id: NgRanTargetId
        :param target_serving_nf_id: The target_serving_nf_id of this SmContextUpdateData.  # noqa: E501
        :type target_serving_nf_id: NfInstanceId
        :param sm_context_status_uri: The sm_context_status_uri of this SmContextUpdateData.  # noqa: E501
        :type sm_context_status_uri: Uri
        :param data_forwarding: The data_forwarding of this SmContextUpdateData.  # noqa: E501
        :type data_forwarding: bool
        :param eps_bearer_setup: The eps_bearer_setup of this SmContextUpdateData.  # noqa: E501
        :type eps_bearer_setup: List[EpsBearerContainer]
        :param revoke_ebi_list: The revoke_ebi_list of this SmContextUpdateData.  # noqa: E501
        :type revoke_ebi_list: List[EpsBearerId]
        :param release: The release of this SmContextUpdateData.  # noqa: E501
        :type release: bool
        :param cause: The cause of this SmContextUpdateData.  # noqa: E501
        :type cause: Cause
        :param ng_ap_cause: The ng_ap_cause of this SmContextUpdateData.  # noqa: E501
        :type ng_ap_cause: NgApCause
        :param _5g_mm_cause_value: The _5g_mm_cause_value of this SmContextUpdateData.  # noqa: E501
        :type _5g_mm_cause_value: Model5GMmCause
        :param s_nssai: The s_nssai of this SmContextUpdateData.  # noqa: E501
        :type s_nssai: Snssai
        :param trace_data: The trace_data of this SmContextUpdateData.  # noqa: E501
        :type trace_data: TraceData
        :param eps_interworking_ind: The eps_interworking_ind of this SmContextUpdateData.  # noqa: E501
        :type eps_interworking_ind: EpsInterworkingIndication
        :param an_type_can_be_changed: The an_type_can_be_changed of this SmContextUpdateData.  # noqa: E501
        :type an_type_can_be_changed: bool
        :param n2_sm_info_ext1: The n2_sm_info_ext1 of this SmContextUpdateData.  # noqa: E501
        :type n2_sm_info_ext1: RefToBinaryData
        :param n2_sm_info_type_ext1: The n2_sm_info_type_ext1 of this SmContextUpdateData.  # noqa: E501
        :type n2_sm_info_type_ext1: N2SmInfoType
        """
        self.swagger_types = {
            'pei': Pei,
            'serving_nf_id': NfInstanceId,
            'guami': Guami,
            'serving_network': PlmnId,
            'backup_amf_info': List[BackupAmfInfo],
            'an_type': AccessType,
            'rat_type': RatType,
            'presence_in_ladn': PresenceState,
            'ue_location': UserLocation,
            'ue_time_zone': TimeZone,
            'add_ue_location': UserLocation,
            'up_cnx_state': UpCnxState,
            'ho_state': HoState,
            'to_be_switched': bool,
            'failed_to_be_switched': bool,
            'n1_sm_msg': RefToBinaryData,
            'n2_sm_info': RefToBinaryData,
            'n2_sm_info_type': N2SmInfoType,
            'target_id': NgRanTargetId,
            'target_serving_nf_id': NfInstanceId,
            'sm_context_status_uri': Uri,
            'data_forwarding': bool,
            'eps_bearer_setup': List[EpsBearerContainer],
            'revoke_ebi_list': List[EpsBearerId],
            'release': bool,
            'cause': Cause,
            'ng_ap_cause': NgApCause,
            '_5g_mm_cause_value': Model5GMmCause,
            's_nssai': Snssai,
            'trace_data': TraceData,
            'eps_interworking_ind': EpsInterworkingIndication,
            'an_type_can_be_changed': bool,
            'n2_sm_info_ext1': RefToBinaryData,
            'n2_sm_info_type_ext1': N2SmInfoType
        }

        self.attribute_map = {
            'pei': 'pei',
            'serving_nf_id': 'servingNfId',
            'guami': 'guami',
            'serving_network': 'servingNetwork',
            'backup_amf_info': 'backupAmfInfo',
            'an_type': 'anType',
            'rat_type': 'ratType',
            'presence_in_ladn': 'presenceInLadn',
            'ue_location': 'ueLocation',
            'ue_time_zone': 'ueTimeZone',
            'add_ue_location': 'addUeLocation',
            'up_cnx_state': 'upCnxState',
            'ho_state': 'hoState',
            'to_be_switched': 'toBeSwitched',
            'failed_to_be_switched': 'failedToBeSwitched',
            'n1_sm_msg': 'n1SmMsg',
            'n2_sm_info': 'n2SmInfo',
            'n2_sm_info_type': 'n2SmInfoType',
            'target_id': 'targetId',
            'target_serving_nf_id': 'targetServingNfId',
            'sm_context_status_uri': 'smContextStatusUri',
            'data_forwarding': 'dataForwarding',
            'eps_bearer_setup': 'epsBearerSetup',
            'revoke_ebi_list': 'revokeEbiList',
            'release': 'release',
            'cause': 'cause',
            'ng_ap_cause': 'ngApCause',
            '_5g_mm_cause_value': '5gMmCauseValue',
            's_nssai': 'sNssai',
            'trace_data': 'traceData',
            'eps_interworking_ind': 'epsInterworkingInd',
            'an_type_can_be_changed': 'anTypeCanBeChanged',
            'n2_sm_info_ext1': 'n2SmInfoExt1',
            'n2_sm_info_type_ext1': 'n2SmInfoTypeExt1'
        }
        self._pei = pei
        self._serving_nf_id = serving_nf_id
        self._guami = guami
        self._serving_network = serving_network
        self._backup_amf_info = backup_amf_info
        self._an_type = an_type
        self._rat_type = rat_type
        self._presence_in_ladn = presence_in_ladn
        self._ue_location = ue_location
        self._ue_time_zone = ue_time_zone
        self._add_ue_location = add_ue_location
        self._up_cnx_state = up_cnx_state
        self._ho_state = ho_state
        self._to_be_switched = to_be_switched
        self._failed_to_be_switched = failed_to_be_switched
        self._n1_sm_msg = n1_sm_msg
        self._n2_sm_info = n2_sm_info
        self._n2_sm_info_type = n2_sm_info_type
        self._target_id = target_id
        self._target_serving_nf_id = target_serving_nf_id
        self._sm_context_status_uri = sm_context_status_uri
        self._data_forwarding = data_forwarding
        self._eps_bearer_setup = eps_bearer_setup
        self._revoke_ebi_list = revoke_ebi_list
        self._release = release
        self._cause = cause
        self._ng_ap_cause = ng_ap_cause
        self.__5g_mm_cause_value = _5g_mm_cause_value
        self._s_nssai = s_nssai
        self._trace_data = trace_data
        self._eps_interworking_ind = eps_interworking_ind
        self._an_type_can_be_changed = an_type_can_be_changed
        self._n2_sm_info_ext1 = n2_sm_info_ext1
        self._n2_sm_info_type_ext1 = n2_sm_info_type_ext1

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SmContextUpdateData of this SmContextUpdateData.  # noqa: E501
        :rtype: SmContextUpdateData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pei(self):
        """Gets the pei of this SmContextUpdateData.


        :return: The pei of this SmContextUpdateData.
        :rtype: Pei
        """
        return self._pei

    @pei.setter
    def pei(self, pei):
        """Sets the pei of this SmContextUpdateData.


        :param pei: The pei of this SmContextUpdateData.
        :type pei: Pei
        """

        self._pei = pei

    @property
    def serving_nf_id(self):
        """Gets the serving_nf_id of this SmContextUpdateData.


        :return: The serving_nf_id of this SmContextUpdateData.
        :rtype: NfInstanceId
        """
        return self._serving_nf_id

    @serving_nf_id.setter
    def serving_nf_id(self, serving_nf_id):
        """Sets the serving_nf_id of this SmContextUpdateData.


        :param serving_nf_id: The serving_nf_id of this SmContextUpdateData.
        :type serving_nf_id: NfInstanceId
        """

        self._serving_nf_id = serving_nf_id

    @property
    def guami(self):
        """Gets the guami of this SmContextUpdateData.


        :return: The guami of this SmContextUpdateData.
        :rtype: Guami
        """
        return self._guami

    @guami.setter
    def guami(self, guami):
        """Sets the guami of this SmContextUpdateData.


        :param guami: The guami of this SmContextUpdateData.
        :type guami: Guami
        """

        self._guami = guami

    @property
    def serving_network(self):
        """Gets the serving_network of this SmContextUpdateData.


        :return: The serving_network of this SmContextUpdateData.
        :rtype: PlmnId
        """
        return self._serving_network

    @serving_network.setter
    def serving_network(self, serving_network):
        """Sets the serving_network of this SmContextUpdateData.


        :param serving_network: The serving_network of this SmContextUpdateData.
        :type serving_network: PlmnId
        """

        self._serving_network = serving_network

    @property
    def backup_amf_info(self):
        """Gets the backup_amf_info of this SmContextUpdateData.


        :return: The backup_amf_info of this SmContextUpdateData.
        :rtype: List[BackupAmfInfo]
        """
        return self._backup_amf_info

    @backup_amf_info.setter
    def backup_amf_info(self, backup_amf_info):
        """Sets the backup_amf_info of this SmContextUpdateData.


        :param backup_amf_info: The backup_amf_info of this SmContextUpdateData.
        :type backup_amf_info: List[BackupAmfInfo]
        """

        self._backup_amf_info = backup_amf_info

    @property
    def an_type(self):
        """Gets the an_type of this SmContextUpdateData.


        :return: The an_type of this SmContextUpdateData.
        :rtype: AccessType
        """
        return self._an_type

    @an_type.setter
    def an_type(self, an_type):
        """Sets the an_type of this SmContextUpdateData.


        :param an_type: The an_type of this SmContextUpdateData.
        :type an_type: AccessType
        """

        self._an_type = an_type

    @property
    def rat_type(self):
        """Gets the rat_type of this SmContextUpdateData.


        :return: The rat_type of this SmContextUpdateData.
        :rtype: RatType
        """
        return self._rat_type

    @rat_type.setter
    def rat_type(self, rat_type):
        """Sets the rat_type of this SmContextUpdateData.


        :param rat_type: The rat_type of this SmContextUpdateData.
        :type rat_type: RatType
        """

        self._rat_type = rat_type

    @property
    def presence_in_ladn(self):
        """Gets the presence_in_ladn of this SmContextUpdateData.


        :return: The presence_in_ladn of this SmContextUpdateData.
        :rtype: PresenceState
        """
        return self._presence_in_ladn

    @presence_in_ladn.setter
    def presence_in_ladn(self, presence_in_ladn):
        """Sets the presence_in_ladn of this SmContextUpdateData.


        :param presence_in_ladn: The presence_in_ladn of this SmContextUpdateData.
        :type presence_in_ladn: PresenceState
        """

        self._presence_in_ladn = presence_in_ladn

    @property
    def ue_location(self):
        """Gets the ue_location of this SmContextUpdateData.


        :return: The ue_location of this SmContextUpdateData.
        :rtype: UserLocation
        """
        return self._ue_location

    @ue_location.setter
    def ue_location(self, ue_location):
        """Sets the ue_location of this SmContextUpdateData.


        :param ue_location: The ue_location of this SmContextUpdateData.
        :type ue_location: UserLocation
        """

        self._ue_location = ue_location

    @property
    def ue_time_zone(self):
        """Gets the ue_time_zone of this SmContextUpdateData.


        :return: The ue_time_zone of this SmContextUpdateData.
        :rtype: TimeZone
        """
        return self._ue_time_zone

    @ue_time_zone.setter
    def ue_time_zone(self, ue_time_zone):
        """Sets the ue_time_zone of this SmContextUpdateData.


        :param ue_time_zone: The ue_time_zone of this SmContextUpdateData.
        :type ue_time_zone: TimeZone
        """

        self._ue_time_zone = ue_time_zone

    @property
    def add_ue_location(self):
        """Gets the add_ue_location of this SmContextUpdateData.


        :return: The add_ue_location of this SmContextUpdateData.
        :rtype: UserLocation
        """
        return self._add_ue_location

    @add_ue_location.setter
    def add_ue_location(self, add_ue_location):
        """Sets the add_ue_location of this SmContextUpdateData.


        :param add_ue_location: The add_ue_location of this SmContextUpdateData.
        :type add_ue_location: UserLocation
        """

        self._add_ue_location = add_ue_location

    @property
    def up_cnx_state(self):
        """Gets the up_cnx_state of this SmContextUpdateData.


        :return: The up_cnx_state of this SmContextUpdateData.
        :rtype: UpCnxState
        """
        return self._up_cnx_state

    @up_cnx_state.setter
    def up_cnx_state(self, up_cnx_state):
        """Sets the up_cnx_state of this SmContextUpdateData.


        :param up_cnx_state: The up_cnx_state of this SmContextUpdateData.
        :type up_cnx_state: UpCnxState
        """

        self._up_cnx_state = up_cnx_state

    @property
    def ho_state(self):
        """Gets the ho_state of this SmContextUpdateData.


        :return: The ho_state of this SmContextUpdateData.
        :rtype: HoState
        """
        return self._ho_state

    @ho_state.setter
    def ho_state(self, ho_state):
        """Sets the ho_state of this SmContextUpdateData.


        :param ho_state: The ho_state of this SmContextUpdateData.
        :type ho_state: HoState
        """

        self._ho_state = ho_state

    @property
    def to_be_switched(self):
        """Gets the to_be_switched of this SmContextUpdateData.


        :return: The to_be_switched of this SmContextUpdateData.
        :rtype: bool
        """
        return self._to_be_switched

    @to_be_switched.setter
    def to_be_switched(self, to_be_switched):
        """Sets the to_be_switched of this SmContextUpdateData.


        :param to_be_switched: The to_be_switched of this SmContextUpdateData.
        :type to_be_switched: bool
        """

        self._to_be_switched = to_be_switched

    @property
    def failed_to_be_switched(self):
        """Gets the failed_to_be_switched of this SmContextUpdateData.


        :return: The failed_to_be_switched of this SmContextUpdateData.
        :rtype: bool
        """
        return self._failed_to_be_switched

    @failed_to_be_switched.setter
    def failed_to_be_switched(self, failed_to_be_switched):
        """Sets the failed_to_be_switched of this SmContextUpdateData.


        :param failed_to_be_switched: The failed_to_be_switched of this SmContextUpdateData.
        :type failed_to_be_switched: bool
        """

        self._failed_to_be_switched = failed_to_be_switched

    @property
    def n1_sm_msg(self):
        """Gets the n1_sm_msg of this SmContextUpdateData.


        :return: The n1_sm_msg of this SmContextUpdateData.
        :rtype: RefToBinaryData
        """
        return self._n1_sm_msg

    @n1_sm_msg.setter
    def n1_sm_msg(self, n1_sm_msg):
        """Sets the n1_sm_msg of this SmContextUpdateData.


        :param n1_sm_msg: The n1_sm_msg of this SmContextUpdateData.
        :type n1_sm_msg: RefToBinaryData
        """

        self._n1_sm_msg = n1_sm_msg

    @property
    def n2_sm_info(self):
        """Gets the n2_sm_info of this SmContextUpdateData.


        :return: The n2_sm_info of this SmContextUpdateData.
        :rtype: RefToBinaryData
        """
        return self._n2_sm_info

    @n2_sm_info.setter
    def n2_sm_info(self, n2_sm_info):
        """Sets the n2_sm_info of this SmContextUpdateData.


        :param n2_sm_info: The n2_sm_info of this SmContextUpdateData.
        :type n2_sm_info: RefToBinaryData
        """

        self._n2_sm_info = n2_sm_info

    @property
    def n2_sm_info_type(self):
        """Gets the n2_sm_info_type of this SmContextUpdateData.


        :return: The n2_sm_info_type of this SmContextUpdateData.
        :rtype: N2SmInfoType
        """
        return self._n2_sm_info_type

    @n2_sm_info_type.setter
    def n2_sm_info_type(self, n2_sm_info_type):
        """Sets the n2_sm_info_type of this SmContextUpdateData.


        :param n2_sm_info_type: The n2_sm_info_type of this SmContextUpdateData.
        :type n2_sm_info_type: N2SmInfoType
        """

        self._n2_sm_info_type = n2_sm_info_type

    @property
    def target_id(self):
        """Gets the target_id of this SmContextUpdateData.


        :return: The target_id of this SmContextUpdateData.
        :rtype: NgRanTargetId
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this SmContextUpdateData.


        :param target_id: The target_id of this SmContextUpdateData.
        :type target_id: NgRanTargetId
        """

        self._target_id = target_id

    @property
    def target_serving_nf_id(self):
        """Gets the target_serving_nf_id of this SmContextUpdateData.


        :return: The target_serving_nf_id of this SmContextUpdateData.
        :rtype: NfInstanceId
        """
        return self._target_serving_nf_id

    @target_serving_nf_id.setter
    def target_serving_nf_id(self, target_serving_nf_id):
        """Sets the target_serving_nf_id of this SmContextUpdateData.


        :param target_serving_nf_id: The target_serving_nf_id of this SmContextUpdateData.
        :type target_serving_nf_id: NfInstanceId
        """

        self._target_serving_nf_id = target_serving_nf_id

    @property
    def sm_context_status_uri(self):
        """Gets the sm_context_status_uri of this SmContextUpdateData.


        :return: The sm_context_status_uri of this SmContextUpdateData.
        :rtype: Uri
        """
        return self._sm_context_status_uri

    @sm_context_status_uri.setter
    def sm_context_status_uri(self, sm_context_status_uri):
        """Sets the sm_context_status_uri of this SmContextUpdateData.


        :param sm_context_status_uri: The sm_context_status_uri of this SmContextUpdateData.
        :type sm_context_status_uri: Uri
        """

        self._sm_context_status_uri = sm_context_status_uri

    @property
    def data_forwarding(self):
        """Gets the data_forwarding of this SmContextUpdateData.


        :return: The data_forwarding of this SmContextUpdateData.
        :rtype: bool
        """
        return self._data_forwarding

    @data_forwarding.setter
    def data_forwarding(self, data_forwarding):
        """Sets the data_forwarding of this SmContextUpdateData.


        :param data_forwarding: The data_forwarding of this SmContextUpdateData.
        :type data_forwarding: bool
        """

        self._data_forwarding = data_forwarding

    @property
    def eps_bearer_setup(self):
        """Gets the eps_bearer_setup of this SmContextUpdateData.


        :return: The eps_bearer_setup of this SmContextUpdateData.
        :rtype: List[EpsBearerContainer]
        """
        return self._eps_bearer_setup

    @eps_bearer_setup.setter
    def eps_bearer_setup(self, eps_bearer_setup):
        """Sets the eps_bearer_setup of this SmContextUpdateData.


        :param eps_bearer_setup: The eps_bearer_setup of this SmContextUpdateData.
        :type eps_bearer_setup: List[EpsBearerContainer]
        """

        self._eps_bearer_setup = eps_bearer_setup

    @property
    def revoke_ebi_list(self):
        """Gets the revoke_ebi_list of this SmContextUpdateData.


        :return: The revoke_ebi_list of this SmContextUpdateData.
        :rtype: List[EpsBearerId]
        """
        return self._revoke_ebi_list

    @revoke_ebi_list.setter
    def revoke_ebi_list(self, revoke_ebi_list):
        """Sets the revoke_ebi_list of this SmContextUpdateData.


        :param revoke_ebi_list: The revoke_ebi_list of this SmContextUpdateData.
        :type revoke_ebi_list: List[EpsBearerId]
        """

        self._revoke_ebi_list = revoke_ebi_list

    @property
    def release(self):
        """Gets the release of this SmContextUpdateData.


        :return: The release of this SmContextUpdateData.
        :rtype: bool
        """
        return self._release

    @release.setter
    def release(self, release):
        """Sets the release of this SmContextUpdateData.


        :param release: The release of this SmContextUpdateData.
        :type release: bool
        """

        self._release = release

    @property
    def cause(self):
        """Gets the cause of this SmContextUpdateData.


        :return: The cause of this SmContextUpdateData.
        :rtype: Cause
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """Sets the cause of this SmContextUpdateData.


        :param cause: The cause of this SmContextUpdateData.
        :type cause: Cause
        """

        self._cause = cause

    @property
    def ng_ap_cause(self):
        """Gets the ng_ap_cause of this SmContextUpdateData.


        :return: The ng_ap_cause of this SmContextUpdateData.
        :rtype: NgApCause
        """
        return self._ng_ap_cause

    @ng_ap_cause.setter
    def ng_ap_cause(self, ng_ap_cause):
        """Sets the ng_ap_cause of this SmContextUpdateData.


        :param ng_ap_cause: The ng_ap_cause of this SmContextUpdateData.
        :type ng_ap_cause: NgApCause
        """

        self._ng_ap_cause = ng_ap_cause

    @property
    def _5g_mm_cause_value(self):
        """Gets the _5g_mm_cause_value of this SmContextUpdateData.


        :return: The _5g_mm_cause_value of this SmContextUpdateData.
        :rtype: Model5GMmCause
        """
        return self.__5g_mm_cause_value

    @_5g_mm_cause_value.setter
    def _5g_mm_cause_value(self, _5g_mm_cause_value):
        """Sets the _5g_mm_cause_value of this SmContextUpdateData.


        :param _5g_mm_cause_value: The _5g_mm_cause_value of this SmContextUpdateData.
        :type _5g_mm_cause_value: Model5GMmCause
        """

        self.__5g_mm_cause_value = _5g_mm_cause_value

    @property
    def s_nssai(self):
        """Gets the s_nssai of this SmContextUpdateData.


        :return: The s_nssai of this SmContextUpdateData.
        :rtype: Snssai
        """
        return self._s_nssai

    @s_nssai.setter
    def s_nssai(self, s_nssai):
        """Sets the s_nssai of this SmContextUpdateData.


        :param s_nssai: The s_nssai of this SmContextUpdateData.
        :type s_nssai: Snssai
        """

        self._s_nssai = s_nssai

    @property
    def trace_data(self):
        """Gets the trace_data of this SmContextUpdateData.


        :return: The trace_data of this SmContextUpdateData.
        :rtype: TraceData
        """
        return self._trace_data

    @trace_data.setter
    def trace_data(self, trace_data):
        """Sets the trace_data of this SmContextUpdateData.


        :param trace_data: The trace_data of this SmContextUpdateData.
        :type trace_data: TraceData
        """

        self._trace_data = trace_data

    @property
    def eps_interworking_ind(self):
        """Gets the eps_interworking_ind of this SmContextUpdateData.


        :return: The eps_interworking_ind of this SmContextUpdateData.
        :rtype: EpsInterworkingIndication
        """
        return self._eps_interworking_ind

    @eps_interworking_ind.setter
    def eps_interworking_ind(self, eps_interworking_ind):
        """Sets the eps_interworking_ind of this SmContextUpdateData.


        :param eps_interworking_ind: The eps_interworking_ind of this SmContextUpdateData.
        :type eps_interworking_ind: EpsInterworkingIndication
        """

        self._eps_interworking_ind = eps_interworking_ind

    @property
    def an_type_can_be_changed(self):
        """Gets the an_type_can_be_changed of this SmContextUpdateData.


        :return: The an_type_can_be_changed of this SmContextUpdateData.
        :rtype: bool
        """
        return self._an_type_can_be_changed

    @an_type_can_be_changed.setter
    def an_type_can_be_changed(self, an_type_can_be_changed):
        """Sets the an_type_can_be_changed of this SmContextUpdateData.


        :param an_type_can_be_changed: The an_type_can_be_changed of this SmContextUpdateData.
        :type an_type_can_be_changed: bool
        """

        self._an_type_can_be_changed = an_type_can_be_changed

    @property
    def n2_sm_info_ext1(self):
        """Gets the n2_sm_info_ext1 of this SmContextUpdateData.


        :return: The n2_sm_info_ext1 of this SmContextUpdateData.
        :rtype: RefToBinaryData
        """
        return self._n2_sm_info_ext1

    @n2_sm_info_ext1.setter
    def n2_sm_info_ext1(self, n2_sm_info_ext1):
        """Sets the n2_sm_info_ext1 of this SmContextUpdateData.


        :param n2_sm_info_ext1: The n2_sm_info_ext1 of this SmContextUpdateData.
        :type n2_sm_info_ext1: RefToBinaryData
        """

        self._n2_sm_info_ext1 = n2_sm_info_ext1

    @property
    def n2_sm_info_type_ext1(self):
        """Gets the n2_sm_info_type_ext1 of this SmContextUpdateData.


        :return: The n2_sm_info_type_ext1 of this SmContextUpdateData.
        :rtype: N2SmInfoType
        """
        return self._n2_sm_info_type_ext1

    @n2_sm_info_type_ext1.setter
    def n2_sm_info_type_ext1(self, n2_sm_info_type_ext1):
        """Sets the n2_sm_info_type_ext1 of this SmContextUpdateData.


        :param n2_sm_info_type_ext1: The n2_sm_info_type_ext1 of this SmContextUpdateData.
        :type n2_sm_info_type_ext1: N2SmInfoType
        """

        self._n2_sm_info_type_ext1 = n2_sm_info_type_ext1
