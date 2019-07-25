import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.models.body2 import Body2  # noqa: E501
from swagger_server.models.body3 import Body3  # noqa: E501
from swagger_server.models.body4 import Body4  # noqa: E501
from swagger_server.models.hsmf_update_data import HsmfUpdateData  # noqa: E501
from swagger_server.models.hsmf_update_error import HsmfUpdateError  # noqa: E501
from swagger_server.models.hsmf_updated_data import HsmfUpdatedData  # noqa: E501
from swagger_server.models.pdu_session_create_data import PduSessionCreateData  # noqa: E501
from swagger_server.models.pdu_session_create_error import PduSessionCreateError  # noqa: E501
from swagger_server.models.pdu_session_created_data import PduSessionCreatedData  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.models.release_data import ReleaseData  # noqa: E501
from swagger_server.models.sm_context_create_error import SmContextCreateError  # noqa: E501
from swagger_server.models.sm_context_created_data import SmContextCreatedData  # noqa: E501
from swagger_server.models.sm_context_release_data import SmContextReleaseData  # noqa: E501
from swagger_server.models.sm_context_retrieve_data import SmContextRetrieveData  # noqa: E501
from swagger_server.models.sm_context_retrieved_data import SmContextRetrievedData  # noqa: E501
from swagger_server.models.sm_context_update_data import SmContextUpdateData  # noqa: E501
from swagger_server.models.sm_context_update_error import SmContextUpdateError  # noqa: E501
from swagger_server.models.sm_context_updated_data import SmContextUpdatedData  # noqa: E501
from swagger_server import util


def post_pdu_sessions(body):  # noqa: E501
    """Create

     # noqa: E501

    :param body: representation of the PDU session to be created in the H-SMF
    :type body: dict | bytes

    :rtype: PduSessionCreatedData
    """
    if connexion.request.is_json:
        body = PduSessionCreateData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_sm_contexts(body):  # noqa: E501
    """Create SM Context

     # noqa: E501

    :param body: representation of the SM context to be created in the SMF
    :type body: dict | bytes

    :rtype: SmContextCreatedData
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def release_pdu_session(pdu_session_ref, body=None):  # noqa: E501
    """Release

     # noqa: E501

    :param pdu_session_ref: PDU session reference
    :type pdu_session_ref: str
    :param body: representation of the data to be sent to H-SMF when releasing the PDU session
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ReleaseData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def release_sm_context(sm_context_ref, body=None):  # noqa: E501
    """Release SM Context

     # noqa: E501

    :param sm_context_ref: SM context reference
    :type sm_context_ref: str
    :param body: representation of the data to be sent to the SMF when releasing the SM context
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = SmContextReleaseData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def retrieve_sm_context(sm_context_ref, body=None):  # noqa: E501
    """Retrieve SM Context

     # noqa: E501

    :param sm_context_ref: SM context reference
    :type sm_context_ref: str
    :param body: parameters used to retrieve the SM context
    :type body: dict | bytes

    :rtype: SmContextRetrievedData
    """
    if connexion.request.is_json:
        body = SmContextRetrieveData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_pdu_session(body, pdu_session_ref):  # noqa: E501
    """Update (initiated by V-SMF)

     # noqa: E501

    :param body: representation of the updates to apply to the PDU session
    :type body: dict | bytes
    :param pdu_session_ref: PDU session reference
    :type pdu_session_ref: str

    :rtype: HsmfUpdatedData
    """
    if connexion.request.is_json:
        body = HsmfUpdateData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_sm_context(body, sm_context_ref):  # noqa: E501
    """Update SM Context

     # noqa: E501

    :param body: representation of the updates to apply to the SM context
    :type body: dict | bytes
    :param sm_context_ref: SM context reference
    :type sm_context_ref: str

    :rtype: SmContextUpdatedData
    """
    if connexion.request.is_json:
        body = SmContextUpdateData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
