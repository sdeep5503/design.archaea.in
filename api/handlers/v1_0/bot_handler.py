from flask import Blueprint, request
from api.services.jwt_auth_service import JWTAuthService
from api.common_helper.common_constants import ApiVersions
from api.services.bot_service import BotService
from api.services.account_service import AccountsService
from api.services.account_user_service import AccountUserService
from api.common_helper.common_validations import RequestValidator
from api.common_helper.http_response import HttpResponse
from api.common_helper.transformers import Transformer

bot_handler = Blueprint(__name__, __name__)


@bot_handler.route(ApiVersions.API_VERSION_V1 + '/accounts/<account_guid>/bots', methods=['POST'])
@RequestValidator.validate_request_header
@JWTAuthService.jwt_validation
def create_bot(account_guid, **kwargs):
    """

    The payload example:

    {
      'name' : 'Account Name'
      'description' : 'About the app'
      'metadata': 'Most Important data'
    }

    :return:
    """
    try:
        bot_name = request.json['name']
        bot_description = request.json['description']
        bot_metadata = str(request.json['metadata'])
        if not bot_name or not bot_description or not bot_metadata:
            return HttpResponse.bad_request('Incomplete parameters. Please provide all the parameters')
        current_user = kwargs['current_user']
        account = AccountsService.get_account_by_guid(account_guid=account_guid)
        if not account:
            return HttpResponse.forbidden('Unexpected request')
        user_permission = AccountUserService.get_permission(user=current_user, account=account)
        if not user_permission:
            return HttpResponse.forbidden('User doesn\'t have permission to perform this operation')
        BotService.create_bot(account=account,
                                             bot_name=bot_name,
                                             bot_metadata=bot_metadata,
                                             user=current_user)
        return HttpResponse.accepted('Bot entry created in design db. This doesn\'t mean bot has been created.')
    except Exception as e:
        return HttpResponse.bad_request(e.message)


@bot_handler.route(ApiVersions.API_VERSION_V1 + '/accounts/<account_guid>/bots', methods=['GET'])
@RequestValidator.validate_request_header
@JWTAuthService.jwt_validation
def get_bots(account_guid, **kwargs):
    """
    GET on accounts

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
            bots = BotService.read(account=account, user=current_user)
            return HttpResponse.success(Transformer.bot_list_to_json_array(bots))
    except Exception as e:
        return HttpResponse.internal_server_error(e.message)

