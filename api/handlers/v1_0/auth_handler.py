from flask import Blueprint, request, make_response, jsonify
from api.services.user_service import UserService
from api.services.token_service import TokenService
from api.common_helper.http_response import HttpResponse
from api.common_helper.common_constants import ApiVersions
from api.common_helper.common_validations import RequestValidator

auth_handler = Blueprint(__name__, __name__)


@auth_handler.route(ApiVersions.API_VERSION_V1 + '/authenticate', methods=['POST'])
@RequestValidator.validate_request_header
def authenticate():
    email = request.json['email']
    password = request.json['password']
    user = None
    try:
        user = UserService.get_user_by_email(email=email)[0]
    except Exception:
        HttpResponse.internal_server_error('Exception while getting the user')
    if user:
        if user.password == password:
            claims_token = TokenService.create_jwt_token(user_guid=user.user_guid)
            response = {
                'claims_token': claims_token
            }
            return HttpResponse.success(response)
    return HttpResponse.unauthorized('Incorrect username or password')