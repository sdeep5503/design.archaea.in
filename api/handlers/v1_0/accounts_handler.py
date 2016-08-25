from flask import Blueprint, request, jsonify
from api.common_helper.common_constants import AccountTypes
from api.services.jwt_auth_service import JWTAuthService
from api.common_helper.common_constants import ApiVersions
from api.services.account_service import AccountsService
from api.common_helper.common_validations import RequestValidator

account_handler = Blueprint(__name__, __name__)


@account_handler.route(ApiVersions.API_VERSION_V1 + '/accounts', methods=['POST'])
@RequestValidator.validate_request_header
@JWTAuthService.jwt_validation
def create_account(**kwargs):
    """
    The payload example:

    {
      'type' : 'Enterprise'/'Niche'/'MarketPlace'
      'name' : 'Account Name'
    }

    :return:
    """
    account_type = request.type['type']
    account_name = request.json['name']
    system_user = kwargs['current_user']
    if system_user.is_system:
        # TODO validate the account name and the type (should be either of AccountTypes)
        AccountsService.create_account(system_user,
                                       account_name=account_name,
                                       account_type=account_type)
    else:
        if account_type == AccountTypes.ENTERPRISE:
            # TODO enterprise accounts should be trail based
            AccountsService.create_account(system_user,
                                           account_name=account_name,
                                           account_type=AccountTypes.ENTERPRISE)
            response = jsonify({
                'message': 'Account created successfully'
            })
            response.status_code = 202
            return response
        else:
            response = jsonify({
                'message': 'You are not allowed to create this account'
            })
            response.status_code = 403
            return response

def get_accounts():
    pass
