from dal.account_user_adapter import AccountUserAdapter
from api.common_helper.common_validations import CommonValidator
from api.common_helper.common_constants import AccountPermissions


class AccountUserService:

    def __init__(self):
        pass

    @staticmethod
    def change_user_permission_on_account(account_guid=None,
                                          user_guid=None,
                                          permission=AccountPermissions.MEMBER):
        """
        This method is used for changing the user permission on a account

        :param account_guid:
        :param user_guid:
        :param permission:
        :return:
        """
        CommonValidator.validate_account_guid(account_guid)
        CommonValidator.validate_user_guid(user_guid)
        AccountUserAdapter.update({
            'account_guid': account_guid,
            'user_guid': user_guid,
        }, permission=permission)

    @staticmethod
    def get_all_accounts_for_given_user(user_guid=None):
        """
        This method returns the list of account guids for a given user guid

        :param user_guid:
        :return:
        """
        CommonValidator.validate_user_guid(user_guid)
        list_of_accounts = AccountUserAdapter.read(user_guid=user_guid)
        return list_of_accounts

