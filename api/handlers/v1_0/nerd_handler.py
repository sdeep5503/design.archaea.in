from flask import Blueprint, request
from api.services.jwt_auth_service import JWTAuthService
from api.common_helper.common_constants import ApiVersions
from api.services.nerd_service import NerdService
from api.services.account_service import AccountsService
from api.services.account_user_service import AccountUserService
from api.common_helper.common_validations import RequestValidator
from api.common_helper.http_response import HttpResponse
from api.common_helper.transformers import Transformer

bot_handler = Blueprint(__name__, __name__)


@bot_handler.route(ApiVersions.API_VERSION_V1 + '/accounts/<account_guid>/nerds', methods=['POST'])
@RequestValidator.validate_request_header
@JWTAuthService.jwt_validation
def create_nerd(account_guid, **kwargs):
    try:
        nerd_name = request.json['name']
        nerd_url = request.json['url']
        current_user = kwargs['current_user']
        account = AccountsService.get_account_by_guid(account_guid=account_guid)
        if not account:
            return HttpResponse.forbidden('The account doesn\'t exist')
        user_permission = AccountUserService.get_permission(user=current_user, account=account)
        if not user_permission:
            return HttpResponse.forbidden('User doesn\'t have permission to perform this operation')
        NerdService.create_nerd(account=account,
                                nerd_name=nerd_name,
                                nerd_url=nerd_url,
                                user=current_user)
        return HttpResponse.accepted('Nerd entry created in design db. This doesn\'t mean bot has been created.')
    except Exception as e:
        return HttpResponse.bad_request(e.message)


@bot_handler.route(ApiVersions.API_VERSION_V1 + '/accounts/<account_guid>/nerds', methods=['GET'])
@RequestValidator.validate_request_header
@JWTAuthService.jwt_validation
def get_nerds(account_guid, **kwargs):
    """
    GET on bots

    :param kwargs:
    :return:
    """
    try:
        current_user = kwargs['current_user']
        account = AccountsService.get_account_by_guid(account_guid=account_guid)
        if not account:
            return HttpResponse.forbidden('Unexpected request')
        user_permission = AccountUserService.get_permission(user=current_user, account=account)
        if not user_permission:
            return HttpResponse.forbidden('User doesn\'t have permission to perform this operation')
        if current_user.is_system:
            return HttpResponse.accepted('All accounts should be returned [unimplemented]')
        else:
            bots = NerdService.read(account=account, user=current_user)
            return HttpResponse.success(Transformer.nerd_list_to_json_array(bots))
    except Exception as e:
        return HttpResponse.internal_server_error(e.message)


@bot_handler.route(ApiVersions.API_VERSION_V1 + '/accounts/<account_guid>/nerds/<nerd_guid>', methods=['GET'])
@RequestValidator.validate_request_header
@JWTAuthService.jwt_validation
def get_nerd_by_guid(account_guid, nerd_guid, **kwargs):
    """
    GET on accounts by account_guid

    :param bot_guid:
    :param account_guid:
    :param kwargs:
    :return:
    """
    try:
        current_user = kwargs['current_user']
        account = AccountsService.get_account_by_guid(account_guid=account_guid)
        if not account:
            return HttpResponse.forbidden('Unexpected request')
        user_permission = AccountUserService.get_permission(user=current_user, account=account)
        if not user_permission:
            return HttpResponse.forbidden('User doesn\'t have permission to perform this operation')
        if current_user.is_system:
            return HttpResponse.accepted('All accounts should be returned [unimplemented]')
        else:
            bots = NerdService.get_nerd_guid(account=account, user=current_user, nerd_guid=nerd_guid)
            if len(bots) == 0:
                return HttpResponse.bad_request('The bot you are looking for is not found in this account')
            return HttpResponse.success(Transformer.nerd_to_json(bots[0]))
    except Exception as e:
        return HttpResponse.internal_server_error(e.message)

