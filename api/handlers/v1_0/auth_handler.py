from flask import Blueprint, request, redirect
from api.services.user_service import UserService
from api.services.nerd_service import NerdService
from api.services.token_service import TokenService
from api.services.account_service import AccountsService
from api.common_helper.http_response import HttpResponse
from api.common_helper.common_constants import ApiVersions
from api.common_helper.common_constants import AccountTypes
from api.common_helper.common_validations import RequestValidator

auth_handler = Blueprint(__name__, __name__)


@auth_handler.route(ApiVersions.API_VERSION_V1 + '/authenticate', methods=['POST'])
@RequestValidator.validate_request_header
def authenticate():
    try:
        email = request.json['email']
        password = request.json['password']
        try:
            user = UserService.get_user_by_email(email=email)
            if len(user) == 0:
                return HttpResponse.forbidden('Incorrect username or password')
            if not user[0].is_active:
                return HttpResponse.forbidden('Please activate your account by confirming your activation e-mail')
        except Exception as e:
            return HttpResponse.internal_server_error(e.message)
        if user[0]:
            if user[0].password == password:
                claims_token = TokenService.create_jwt_token(user_guid=user[0].user_guid)
                response = {
                    'claims_token': claims_token
                }
                return HttpResponse.success(response)
        return HttpResponse.unauthorized('Incorrect username or password')
    except Exception as e:
        return HttpResponse.internal_server_error(e.message)


@auth_handler.route(ApiVersions.API_VERSION_V1 + '/users/<user_guid>/confirm', methods=['GET'])
def confirm_user(user_guid):
    try:
        user = UserService.get_user_by_guid(user_guid=user_guid)
        if len(user) == 0:
            return HttpResponse.forbidden('User not found. Please register yourself through Nerdstacks')
        if user[0].is_active:
            return redirect("http://127.0.0.1:9081/login", code=302)
        niche_account = AccountsService.get_account_by_account_type(AccountTypes.COMMON_NICHE)
        if len(niche_account) == 0:
            return HttpResponse.bad_request('No Niche account found')
        NerdService.give_permission_to_nerds_by_account(account=niche_account[0],
                                                        user=user[0])
        UserService.confirm_user(user_guid=user_guid)
        return redirect("http://127.0.0.1:9081/login", code=302)
    except Exception as e:
        return HttpResponse.internal_server_error(e.message)