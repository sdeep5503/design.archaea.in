from models.users import Users
from flask import Blueprint, request, jsonify
from api.services.user_service import UserService
from api.common_helper.http_response import HttpResponse
from api.services.jwt_auth_service import JWTAuthService
from api.services.account_service import AccountsService
from api.common_helper.common_constants import ApiVersions
from api.common_helper.common_validations import RequestValidator

user_handler = Blueprint(__name__, __name__)


@user_handler.route(ApiVersions.API_VERSION_V1 + '/users', methods=['POST'])
@RequestValidator.validate_request_header
def create_niche_user():
    """
    Open API to create Niche Users (Cannot create system users this way)

    The payload example:

    {
      'email': <email>
      'password': <password>
      'first_name': <Name>
      'last_name': <Name>
      'company': <Company>
    }

    :return:
    """
    email = request.json['email']
    password = request.json['password']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    company = request.json['company']

    # TODO validate required fields
    try:
        AccountsService.add_user_to_niche(user=Users(
            user_guid=None,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_system=False,
            company=company
        ))
    except Exception as e:
        HttpResponse.internal_server_error(e.message)
    return HttpResponse.accepted('User added to common niche account successfully')


@user_handler.route(ApiVersions.API_VERSION_V1 + '<account_guid>/users', methods=['PUT'])
@RequestValidator.validate_request_header
@JWTAuthService.jwt_validation
def add_user_to_account(account_guid):
    """
    This api adds users to account

    :param account_guid:
    :return:
    """
    # TODO validate whether the current user is admin of the given account
    new_user = UserService.get_user_by_email(email=request.json['email'])[0]

    if not new_user:
        return HttpResponse.bad_request('This user is unknown to archaea')
    else:
        try:
            AccountsService.add_user_to_account(
                account_guid=account_guid,
                user=new_user
            )
            return HttpResponse.accepted('User has been added successfully')
        except:
            return HttpResponse.internal_server_error('Exception while adding user to account')