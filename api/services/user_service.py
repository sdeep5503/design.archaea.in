from api.services.account_service import AccountsService
from api.common_helper.common_constants import AccountTypes


class UserService:

    def __init__(self):
        pass

    @staticmethod
    def create_new_enterprise_user(user=None,
                                   account_name=None):
        """
        Creating a new user which will add this person to marketplace/common account

        :param user:
        :param account_name:
        :return:
        """
        if not account_name:
            raise Exception('[Services] Please enter valid first name')
        if not user:
            raise Exception('[Services] Please enter valid last name')
        AccountsService.create_account(user=user,
                                       account_name=account_name,
                                       account_type=AccountTypes.ENTERPRISE)
