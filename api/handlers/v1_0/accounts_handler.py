from flask import Blueprint, request
from api.common_helper.common_constants import ApiVersions
from api.common_helper.common_validations import RequestValidator

account_handler = Blueprint(__name__, __name__)


@account_handler.route(ApiVersions.API_VERSION_V1 + '/accounts', methods=['POST'])
@RequestValidator.validate_request_header
def post():
    """
    The payload example:

    {
      'type' : 'Enterprise'/'Niche'/'MarketPlace'
      'name' : 'Account Name'
    }

    :return:
    """
    account_type = request.json['type']
    account_name = request.json['name']
    # TODO create marketplace and niche account if and only if 'system' user
