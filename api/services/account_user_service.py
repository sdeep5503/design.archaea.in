from dal.account_user_adapter import AccountUserAdapter
from api.common_helper.common_validations import CommonValidator
from api.common_helper.common_constants import AccountPermissions


class AccountUserService:

    def __init__(self):
        pass

    @staticmethod
    def change_user_permission_on_account(account_id=None,
                                          user_id=None,
                                          permission=AccountPermissions.MEMBER):
        """
        This method is used for changing the user permission on a account

        :param account_id:
        :param user_id:
        :param permission:
        :return:
        """
        AccountUserAdapter.update({
            'account_id': account_id,
            'user_id': user_id,
        }, permission=permission)

    @staticmethod
    def get_permission(user, account):
        account_permissions = AccountUserAdapter.read(user_id=user.user_id,
                                account_id=account.account_id)
        if len(account_permissions) == 1:
            return account_permissions[0].permission
        else:
            return None

    @staticmethod
    def get_all_accounts_for_given_user(user_id=None):
        """
        This method returns the list of account guids for a given user guid

        :param user_id:
        :return:
        """
        list_of_accounts = AccountUserAdapter.read_by_user_id(user_id=user_id)
        return list_of_accounts

