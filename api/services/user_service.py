from models.users import Users
from validate_email import validate_email
from api.services.account_service import AccountsService
from api.common_helper.password_util import PasswordHelper


class UserService:

    def __init__(self):
        pass

    @staticmethod
    def create_new_user(email=None,
                        password=None,
                        first_name=None,
                        last_name=None,
                        company=None,
                        account_name=None):
        """
        Creating a new user which will add this person to marketplace/common account

        :param email:
        :param password:
        :param first_name:
        :param last_name:
        :param company:
        :param account_name:
        :return:
        """
        if not email or not validate_email(email):
            raise Exception('[Services] Invalid email format')
        if not password or not PasswordHelper.validate_password(password):
            raise Exception('[Services] Invalid email format')
        if not first_name:
            raise Exception('[Services] Please enter valid first name')
        if not last_name:
            raise Exception('[Services] Please enter valid last name')
        AccountsService.create_account(Users(
            user_guid='',
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            company=company
        ), account_name=account_name, is_trail=True, is_enterprise=False)
