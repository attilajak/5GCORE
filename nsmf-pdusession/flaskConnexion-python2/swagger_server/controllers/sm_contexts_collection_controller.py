import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.models.sm_context_create_error import SmContextCreateError  # noqa: E501
from swagger_server.models.sm_context_created_data import SmContextCreatedData  # noqa: E501
from swagger_server import util


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
