from flask import Blueprint, request
from api.common_helper.common_constants import AccountTypes
from api.services.jwt_auth_service import JWTAuthService
from api.common_helper.common_constants import ApiVersions
from api.services.account_service import AccountsService
from api.common_helper.common_validations import RequestValidator
from api.common_helper.http_response import HttpResponse

account_handler = Blueprint(__name__, __name__)


@account_handler.route(ApiVersions.API_VERSION_V1 + '/accounts', methods=['POST'])
@RequestValidator.validate_request_header
@JWTAuthService.jwt_validation
def create_account(**kwargs):
    """
    This API can be used by system user to create Niche account and other users to create enterprise accounts

    The payload example:

    {
      'type' : 'Enterprise'/'Niche'/'MarketPlace'
      'name' : 'Account Name'
    }

    :return:
    """
    account_type = request.type['type']
    account_name = request.json['name']
    if not account_type or not account_name:
        return HttpResponse.bad_request('Incomplete parameters')
    current_user = kwargs['current_user']
    if current_user.is_system:
        try:
            AccountsService.create_account(current_user,
                                           account_name=account_name,
                                           account_type=account_type)
            return HttpResponse.accepted('Account created successfully')
        except Exception:
            return HttpResponse.internal_server_error('Exception while creating account')

    else:
        if account_type == AccountTypes.ENTERPRISE:
            try:
                AccountsService.create_account(current_user,
                                               account_name=account_name,
                                               account_type=AccountTypes.ENTERPRISE)
                return HttpResponse.accepted('Account created successfully')
            except Exception:
                return HttpResponse.internal_server_error('Exception while creating account')
        else:
            return HttpResponse.forbidden('You are not allowed to create this account')
