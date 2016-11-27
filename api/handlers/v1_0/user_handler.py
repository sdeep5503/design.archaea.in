from models.users import Users
from flask import Blueprint, request
from api.services.user_service import UserService
from api.common_helper.http_response import HttpResponse
from api.common_helper.common_utils import CommonHelper
from api.services.jwt_auth_service import JWTAuthService
from api.services.account_service import AccountsService
from api.common_helper.common_constants import ApiVersions, AccountPermissions
from api.common_helper.common_validations import RequestValidator

user_handler = Blueprint(__name__, __name__)


@user_handler.route(ApiVersions.API_VERSION_V1 + '/users', methods=['POST'])
@RequestValidator.validate_request_header
def create_niche_user():
    try:
        try:
            email = request.json['email']
            password = request.json['password']
            first_name = request.json['first_name']
            last_name = request.json['last_name']
            company = request.json['company']
        except Exception:
            return HttpResponse.bad_request('One or parameters are missing')
        AccountsService.add_user_to_niche(user=Users(
            user_guid=CommonHelper.generate_guid(),
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_system=False,
            company=company
        ))
        return HttpResponse.accepted('User added to common niche account successfully')
    except Exception as e:
        HttpResponse.internal_server_error(e.message)


@user_handler.route(ApiVersions.API_VERSION_V1 + '<account_guid>/users', methods=['PUT'])
@RequestValidator.validate_request_header
@JWTAuthService.jwt_validation
def add_user_to_account(account_guid, **kwargs):
    """
    This api adds users to account

    :param account_guid:
    :return:
    """
    try:
        new_user = UserService.get_user_by_email(email=request.json['email'])[0]
        current_user = kwargs['current_user']
        try:
            permission = AccountsService.get_user_permission_on_account(user=current_user, account_guid=account_guid)
            if permission == AccountPermissions.MEMBER:
                HttpResponse.forbidden('User doesn\'t have permission to perform this operation')
        except Exception as e:
            if e.message == '[Services] user doesn\'t have permission on account':
                return HttpResponse.forbidden(e.message)
        if not new_user:
            return HttpResponse.bad_request('This user is unknown to archaea')
        else:
            AccountsService.add_user_to_account(
                account_guid=account_guid,
                user=new_user
            )
            return HttpResponse.accepted('User has been added successfully')
    except Exception as e:
        HttpResponse.internal_server_error(e.message)