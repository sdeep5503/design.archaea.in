from json import loads
from flask import Blueprint, request
from api.services.jwt_auth_service import JWTAuthService
from api.common_helper.common_validations import RequestValidator
from api.common_helper.common_constants import ApiVersions
from api.common_helper.http_response import HttpResponse
from api.services.application_service import ApplicationService
from api.services.account_service import AccountsService
from api.services.account_user_service import AccountUserService
from api.services.nerd_service import NerdService

application_handler = Blueprint(__name__, __name__)


@application_handler.route(ApiVersions.API_VERSION_V1 + '/accounts/<account_guid>/nerds/<nerd_guid>/applications',
                           methods=['POST'])
@RequestValidator.validate_request_header
@JWTAuthService.jwt_validation
def create_application(account_guid, nerd_guid, **kwargs):
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
        nerd = NerdService.get_nerd_guid(account=account, user=current_user, nerd_guid=nerd_guid)
        if len(nerd) == 0:
            return HttpResponse.forbidden('The user has no permission on this nerd')
        nerd_response = ApplicationService.create_application(account_id=account.account_id,
                                                              application_name=name,
                                                              application_algorithm=algorithm,
                                                              created_user_id=current_user.user_id,
                                                              parameters=app_metadata,
                                                              nerd_url=nerd[0].nerd_url)
        return HttpResponse.custom_http_response(loads(nerd_response.text), nerd_response.status_code)
    except Exception as e:
        return HttpResponse.bad_request(e.message)


@application_handler.route(ApiVersions.API_VERSION_V1 + '/accounts/<account_guid>/nerds/<nerd_guid>/applications',
                           methods=['GET'])
@RequestValidator.validate_request_header
@JWTAuthService.jwt_validation
def get_all_applications(account_guid, nerd_guid, **kwargs):
    try:
        current_user = kwargs['current_user']
        account = AccountsService.get_account_by_guid(account_guid=account_guid)
        if not account:
            return HttpResponse.forbidden('Account doesn\'t exists')
        user_permission = AccountUserService.get_permission(user=current_user, account=account)
        if not user_permission:
            return HttpResponse.forbidden('User doesn\'t have permission to perform this operation')
        nerd = NerdService.get_nerd_guid(account=account, user=current_user, nerd_guid=nerd_guid)
        if len(nerd) == 0:
            return HttpResponse.forbidden('The user has no permission on this nerd')
        nerd_response = ApplicationService.get_application(nerd_url=nerd[0].nerd_url)
        return HttpResponse.custom_http_response(loads(nerd_response.text), nerd_response.status_code)
    except Exception as e:
        return HttpResponse.bad_request(e.message)


@application_handler.route(
    ApiVersions.API_VERSION_V1 + '/accounts/<account_guid>/nerds/<nerd_guid>/applications/<application_guid>',
    methods=['GET'])
@RequestValidator.validate_request_header
@JWTAuthService.jwt_validation
def get_application(account_guid, nerd_guid, application_guid, **kwargs):
    try:
        current_user = kwargs['current_user']
        account = AccountsService.get_account_by_guid(account_guid=account_guid)
        if not account:
            return HttpResponse.forbidden('Account doesn\'t exists')
        user_permission = AccountUserService.get_permission(user=current_user, account=account)
        if not user_permission:
            return HttpResponse.forbidden('User doesn\'t have permission to perform this operation')
        nerd = NerdService.get_nerd_guid(account=account, user=current_user, nerd_guid=nerd_guid)
        if len(nerd) == 0:
            return HttpResponse.forbidden('The user has no permission on this nerd')
        nerd_response = ApplicationService.get_application_by_guid(nerd_url=nerd[0].nerd_url,
                                                                   application_guid=application_guid)
        return HttpResponse.custom_http_response(loads(nerd_response.text), nerd_response.status_code)
    except Exception as e:
        return HttpResponse.bad_request(e.message)
