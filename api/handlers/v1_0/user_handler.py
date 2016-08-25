from models.users import Users
from flask import Blueprint, request, jsonify
from api.services.user_service import UserService
from api.services.jwt_auth_service import JWTAuthService
from api.services.account_service import AccountsService
from api.common_helper.common_constants import ApiVersions
from api.common_helper.common_validations import RequestValidator

user_handler = Blueprint(__name__, __name__)


@user_handler.route(ApiVersions.API_VERSION_V1 + '/users', methods=['POST'])
@RequestValidator.validate_request_header
def create_niche_user():
    """
    Open API to create Niche Users

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
    user_guid = None
    AccountsService.add_user_to_niche(user=Users(
        user_guid=None,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        company=company
    ))
    return {
        'user_guid': user_guid
    }


@user_handler.route(ApiVersions.API_VERSION_V1 + '<account_guid>/users', method=['PUT'])
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
        response = jsonify({
            'message': 'This user is unknown to archaea'
        })
        response.status_code = 400
        return response
    else:
        AccountsService.add_user_to_account(
            account_guid=account_guid,
            user=new_user
        )
        response = jsonify({
            'message': 'User has been added successfully'
        })
        response.status_code = 202
        return response