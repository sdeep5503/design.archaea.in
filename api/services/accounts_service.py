from models.users import Users
from dal.user_adapter import UserAdapter
from dal.accounts_adapter import AccountsAdapter
from dal.account_user_adapter import AccountUserAdapter
from api.common_helper.common_utils import CommonHelper
from api.common_helper.common_validations import CommonValidator
from api.services.account_user_service import AccountUserService
from api.common_helper.common_constants import AccountPermissions


class AccountsService:

    def __init__(self):
        pass

    @staticmethod
    def create_account(user=None,
                       account_name=None,
                       is_trail=1,
                       is_enterprise=0):
        """
        This method creates a account and corresponding user and makes the user owner

        :param user:
        :param account_name:
        :param is_trail:
        :param is_enterprise:
        :return:
        """
        if not isinstance(user, Users):
            raise Exception('[Services] User not found while creating account')
        if not account_name or len(account_name) == 0:
            raise Exception('[Services] Account Name should contain atleast one character')
        if is_trail == is_enterprise:
            raise Exception('[Services] Account should be either trail or enterprise, cannot be both')
        existing_user_with_same_email = UserAdapter.read({
            'email': user.email
        })
        new_account_guid = CommonHelper.generate_guid()
        if len(existing_user_with_same_email) == 0:
            AccountsAdapter.create(
                account_name=account_name,
                account_guid=new_account_guid,
                is_active=True,
                is_trail=is_trail,
                is_enterprise=is_enterprise,
                is_deleted=False,
                owner=user)
            AccountUserService.change_user_permission_on_account(user_guid=user.user_guid,
                                                                 account_guid=new_account_guid,
                                                                 permission=AccountPermissions.OWNER)
        else:
            raise Exception('[Services] User cannot create multiple accounts. '
                            'Please add yourself to any other account if needed')
        return new_account_guid

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
    def deactivate_account(account_guid=None):
        """
        This method deactivates an account by fliping is active flag

        :param account_guid:
        :return:
        """
        CommonValidator.validate_account_guid(account_guid)
        AccountsAdapter.update(query={
            'account_guid': account_guid
        }, updated_value={
            'is_active': False
        })

    @staticmethod
    def get_all_accounts_by_user(user_guid=None):
        CommonValidator.validate_user_guid(user_guid=user_guid)
        list_of_accounts = AccountUserAdapter.read(user_guid)
        return list_of_accounts
