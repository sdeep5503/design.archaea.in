from models.users import Users
from dal.accounts_adapter import AccountsAdapter
from dal.account_user_adapter import AccountUserAdapter
from api.common_helper.common_utils import CommonHelper
from api.common_helper.common_constants import AccountTypes
from api.common_helper.common_validations import CommonValidator
from api.services.account_user_service import AccountUserService
from api.common_helper.common_constants import AccountPermissions


class AccountsService:

    def __init__(self):
        pass

    @staticmethod
    def create_account(user=None,
                       account_name=None,
                       account_type=None):
        """
        This method creates a account and corresponding user and makes the user owner

        :param account_type:
        :param user:
        :param account_name:
        :return:
        """
        if not isinstance(user, Users):
            raise Exception('[Services] User<Owner> not found while creating account')
        if not account_name or len(account_name) == 0:
            raise Exception('[Services] Account Name should contain atleast one character')
        new_account_guid = CommonHelper.generate_guid()
        account_id = AccountsAdapter.create(
            account_name=account_name,
            account_guid=new_account_guid,
            account_type=account_type,
            owner=user)
        AccountUserService.change_user_permission_on_account(user_id=user.user_id,
                                                             account_id=account_id,
                                                             permission=AccountPermissions.OWNER)
        return new_account_guid

    @staticmethod
    def get_account_by_guid(account_guid=None):
        """
        Gets the account by userid

        :param account_guid:
        :return:
        """
        account = AccountsAdapter.read({
            'account_guid': account_guid
        })
        if len(account) == 0:
            return None
        return account[0]

    @staticmethod
    def get_all_accounts_by_user(user_id=None):
        """
        This method returns all the accounts of a given user_guid

        :param user_id:
        :return:
        """
        list_of_accounts = AccountUserAdapter.read_by_user_id(user_id=user_id)
        account_id_list = []
        for account in list_of_accounts:
            account_id_list.append(account.account_id)
        account_list = AccountsAdapter.read_accounts_by_id_list(account_id_list)
        return account_list

    @staticmethod
    def update_account(query=None,
                       update_values=None):
        """
        This function updates an account.

        :param query:
        :param update_values:
        :return:
        """
        if not query:
            raise Exception('[Services] Update Query should not be empty')
        if not update_values:
            raise Exception('[Services] Update values should not be empty')
        AccountsAdapter.update(query=query,
                               updated_value=update_values)

    @staticmethod
    def delete_account(account_id=None):
        """
        Soft deleting account

        :param account_id:
        :return:
        """
        if not account_id:
            CommonValidator.validate_account_guid(account_id)
            AccountsAdapter.update(query={
                'account_id': account_id
            }, updated_value={
                'is_deleted': True
            })

    @staticmethod
    def deactivate_account(account_id=None):
        """
        This method deactivates an account by fliping is active flag

        :param account_guid:
        :return:
        """
        CommonValidator.validate_account_guid(account_id)
        AccountsAdapter.update(query={
            'account_id': account_id
        }, updated_value={
            'is_active': False
        })

    @staticmethod
    def add_user_to_account(account_guid=None, user=None):
        """
        This method adds users to account

        :param account_guid:
        :param user:
        :return:
        """
        AccountsAdapter.add_user({
            'account_guid': account_guid
        }, user=user)

    @staticmethod
    def add_user_to_niche(nich_type=AccountTypes.COMMON_NICHE, user=None):
        """
        Add user to Niche

        :param nich_type:
        :param user:
        :return:
        """
        AccountsAdapter.add_user({
            'account_type': nich_type
        }, user=user)

    @staticmethod
    def get_user_permission_on_account(user=None, account_guid=None):
        """
        Returns user permission on account

        :param user:
        :param account_guid:
        :return:
        """
        accounts = AccountsAdapter.read({
            'account_guid': account_guid
        })
        if not accounts or len(accounts) == 0:
            raise Exception('[Services] account not found')
        account_user = AccountUserAdapter.read(user_id=user.user_id,
                                account_id=accounts[0].account_id)
        if not account_user or len(account_user) == 0:
            Exception('[Services] user doesn\'t have permission on account')
        return account_user[0].permission
