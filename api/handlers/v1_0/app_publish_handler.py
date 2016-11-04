from flask import Blueprint, request
from api.services.app_bot_service import AppBotService
from api.common_helper.http_response import HttpResponse
from api.common_helper.common_constants import ApiVersions
from api.services.account_service import AccountsService
from api.services.account_user_service import AccountUserService
from api.services.bot_service import BotService
from api.services.app_publish_service import ApplicationPublishServices
from api.services.applications_service import ApplicationsService

publish_handler = Blueprint(__name__, __name__)

# TODO authentication
@publish_handler.route(
    ApiVersions.API_VERSION_V1 + '/accounts/<account_guid>/applications/<application_guid>/publish',
    methods=['POST'])
def app_publish(account_guid, application_guid, **kwargs):
    try:
        try:
            bot_guid = request.json['bot_guid']
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
        application = ApplicationsService.get_application_by_guid(application_guid=application_guid)
        if len(application) == 0:
            return HttpResponse.forbidden('The user has no permission on this application')
        if application.account_id != account.account_id:
            return HttpResponse.forbidden('The application is not found in the account')
        if AppBotService.is_app_published_on_bot(bot_id=bot.bot_id,
                                                 application_id=application.application_id):
            HttpResponse.bad_request(
                'This application is already published. Please un-publish the same to publish again')
        ApplicationPublishServices.publish_app(application_id=application.application_id,
                                           bot_id=bot.bot_id)
        return HttpResponse.accepted('The application has been published successfully')
    except Exception as e:
        return HttpResponse.internal_server_error(e.message)
