from flask import Blueprint, request
from api.common_helper.common_constants import AccountTypes, ProjectDetails
from api.services.jwt_auth_service import JWTAuthService
from api.common_helper.common_constants import ApiVersions
from api.services.account_service import AccountsService
from api.common_helper.common_validations import RequestValidator
from api.common_helper.http_response import HttpResponse
from api.common_helper.transformers import Transformer

account_handler = Blueprint(__name__, __name__)


@account_handler.route(ApiVersions.API_VERSION_V1 + '/accounts', methods=['POST'])
@RequestValidator.validate_request_header
@JWTAuthService.jwt_validation
def create_account(**kwargs):
    try:
        account_type = request.json['type']
        account_name = request.json['name']
        company = request.json['company']
        if not account_type or not account_name:
            return HttpResponse.bad_request('Incomplete parameters')
        current_user = kwargs['current_user']
        if current_user.is_system:
            AccountsService.create_account(current_user,
                                           company=ProjectDetails.COMPANY_NAME,
                                           account_name=account_name,
                                           account_type=account_type)
            return HttpResponse.accepted('Account created successfully')
        else:
            if account_type == AccountTypes.ENTERPRISE:
                AccountsService.create_account(current_user,
                                               account_name=account_name,
                                               company=company,
                                               account_type=AccountTypes.ENTERPRISE)
                return HttpResponse.accepted('Account created successfully')
            else:
                return HttpResponse.forbidden('You are not allowed to create this account')
    except Exception as e:
        return HttpResponse.bad_request(e.message)


@account_handler.route(ApiVersions.API_VERSION_V1 + '/accounts', methods=['GET'])
@RequestValidator.validate_request_header
@JWTAuthService.jwt_validation
def get_accounts(**kwargs):
    """
    GET on accounts

    :param kwargs:
    :return:
    """
    try:
        current_user = kwargs['current_user']
        if current_user.is_system:
            return HttpResponse.accepted('All accounts should be returned [unimplemented]')
        else:
            accounts = AccountsService.get_all_accounts_by_user(user_id=current_user.user_id)
            return HttpResponse.success(Transformer.account_list_to_json_array(accounts))
    except Exception as e:
        return HttpResponse.internal_server_error(e.message)


@account_handler.route(ApiVersions.API_VERSION_V1 + '/accounts/<account_guid>', methods=['GET'])
@RequestValidator.validate_request_header
@JWTAuthService.jwt_validation
def get_accounts_by_guid(account_guid, **kwargs):
    """
    GET on accounts by account_guid

    :param account_guid:
    :param kwargs:
    :return:
    """
    try:
        current_user = kwargs['current_user']
        try:
            AccountsService.get_user_permission_on_account(user=current_user, account_guid=account_guid)
        except Exception as e:
            if e.message == '[Services] user doesn\'t have permission on account':
                return HttpResponse.forbidden(e.message)
        if current_user.is_system:
            return HttpResponse.accepted('All accounts should be returned [unimplemented]')
        else:
            accounts = AccountsService.get_account_by_guid(account_guid=account_guid)
            if not len(accounts) or len(accounts) == 0:
                return HttpResponse.bad_request('The account doesn\'t exist')
            return HttpResponse.success(Transformer.account_to_json(accounts[0]))
    except Exception as e:
        return HttpResponse.internal_server_error(e.message)
