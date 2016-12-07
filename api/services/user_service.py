from dal.user_adapter import UserAdapter
from api.services.account_service import AccountsService
from api.common_helper.common_utils import CommonHelper


class UserService:

    def __init__(self):
        pass

    @staticmethod
    def create_user_and_add_to_niche(email=None,
                    password=None,
                    first_name=None,
                    last_name=None,
                    company=None):
        user = UserAdapter.create(user_guid=CommonHelper.generate_guid(),
                           email=email,
                           password=password,
                           first_name=first_name,
                           last_name=last_name,
                           company=company)
        AccountsService.add_user_to_niche(user=user)


    @staticmethod
    def get_user_by_email(email=None):
        """
        Reads Users

        :param email:
        :return:
        """
        return UserAdapter.read({
            'email': email
        })

    @staticmethod
    def get_user_by_guid(user_guid=None):
        """
        Reads Users

        :param user_guid:
        :return:
        """
        return UserAdapter.read({
            'user_guid': user_guid
        })
