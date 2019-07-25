import connexion
import six

from swagger_server.models.body3 import Body3  # noqa: E501
from swagger_server.models.pdu_session_create_data import PduSessionCreateData  # noqa: E501
from swagger_server.models.pdu_session_create_error import PduSessionCreateError  # noqa: E501
from swagger_server.models.pdu_session_created_data import PduSessionCreatedData  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
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
