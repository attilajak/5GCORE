import connexion
import six

from swagger_server.models.body4 import Body4  # noqa: E501
from swagger_server.models.hsmf_update_data import HsmfUpdateData  # noqa: E501
from swagger_server.models.hsmf_update_error import HsmfUpdateError  # noqa: E501
from swagger_server.models.hsmf_updated_data import HsmfUpdatedData  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.models.release_data import ReleaseData  # noqa: E501
from swagger_server import util


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
