from json import dumps
from flask import Blueprint, request
from api.services.jwt_auth_service import JWTAuthService
from api.common_helper.common_validations import RequestValidator
from api.common_helper.common_constants import ApiVersions
from api.common_helper.http_response import HttpResponse
from api.services.applications_service import ApplicationsService
from api.services.account_service import AccountsService
from api.services.account_user_service import AccountUserService
from api.services.bot_service import BotService

account_handler = Blueprint(__name__, __name__)


@account_handler.route(ApiVersions.API_VERSION_V1 + '/accounts/<account_guid>/bots/<bot_guid>/applications',
                       methods=['POST'])
@RequestValidator.validate_request_header
@JWTAuthService.jwt_validation
def create_application(account_guid, bot_guid, **kwargs):
    try:
        try:
            name = request.json['name']
            algorithm = request.json['algorithm']
            app_metadata = request.json['app_metadata']
        except Exception:
            return HttpResponse.bad_request('One or more parameters are missing')
        current_user = kwargs['current_user']
        account = AccountsService.get_account_by_guid(account_guid=account_guid)
        if not account:
            return HttpResponse.forbidden('Account doesn\'t exists')
        user_permission = AccountUserService.get_permission(user=current_user, account=account)
        if not user_permission:
            return HttpResponse.forbidden('User doesn\'t have permission to perform this operation')
        bot = BotService.get_bot_guid(account=account, user=current_user, bot_guid=bot_guid)
        if len(bot) == 0:
            return HttpResponse.forbidden('The user has no permission on this bot')
        ApplicationsService.create_application(account_id=account.account_id,
                                               application_name=name,
                                               application_algorithm=algorithm,
                                               user_id=current_user.user_id,
                                               app_metadata=dumps(app_metadata),
                                               bot_id=None)
        return HttpResponse.accepted('Application created successfully')
    except Exception as e:
        return HttpResponse.bad_request(e.message)
