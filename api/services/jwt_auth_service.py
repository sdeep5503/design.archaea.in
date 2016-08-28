from flask import request
from functools import wraps
from token_service import TokenService
from api.services.user_service import UserService
from api.common_helper.common_constants import ApiRequestConstants


class JWTAuthService:
    
    def __init__(self):
        pass

    @staticmethod
    def jwt_validation(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            current_user = JWTAuthService.validate_jwt_token_and_get_user(request.headers
                .get(ApiRequestConstants.X_ARCHAEA_AUTHORIZATION))
            kwargs['current_user'] = current_user
            return f(*args, **kwargs)

        return decorated

    @staticmethod
    def validate_jwt_token_and_get_user(token):
        jwt_token_decoded = TokenService.decode_jwt_token(token)
        # TODO complete the jwt validation (Exp and User Existence etc)
        # TODO Also we can check for user permissions on the API
        user = UserService.get_user_by_guid(user_guid=jwt_token_decoded['_identity'])
        return user
