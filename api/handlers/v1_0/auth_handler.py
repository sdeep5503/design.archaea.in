from flask import Blueprint, request
from api.services.user_service import UserService
from api.services.token_service import TokenService
from api.common_helper.http_response import HttpResponse
from api.common_helper.common_constants import ApiVersions
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
        return HttpResponse.internal_server_error(e.message);