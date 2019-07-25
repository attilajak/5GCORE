import connexion
import six

from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.models.body2 import Body2  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.models.sm_context_release_data import SmContextReleaseData  # noqa: E501
from swagger_server.models.sm_context_retrieve_data import SmContextRetrieveData  # noqa: E501
from swagger_server.models.sm_context_retrieved_data import SmContextRetrievedData  # noqa: E501
from swagger_server.models.sm_context_update_data import SmContextUpdateData  # noqa: E501
from swagger_server.models.sm_context_update_error import SmContextUpdateError  # noqa: E501
from swagger_server.models.sm_context_updated_data import SmContextUpdatedData  # noqa: E501
from swagger_server import util


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
