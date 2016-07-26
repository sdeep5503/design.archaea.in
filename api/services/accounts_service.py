from models.users import Users
from dal.user_adapter import UserAdapter
from dal.accounts_adapter import AccountsAdapter
from api.common_helper.common_utils import CommonHelper
from api.common_helper.common_validations import CommonValidator
from api.services.account_user_service import AccountUserService


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
                                                                 account_guid=new_account_guid)
        else:
            raise Exception('[Services] User cannot create multiple accounts. '
                            'Please add yourself to any other account if needed')
        return new_account_guid

    @staticmethod
    def get_accounts_by_user(user_guid=None):
        CommonValidator.validate_user_guid(user_guid=user_guid)



    @staticmethod
    def deactivate_account(account_guid=None):
        """
        This method deactivates an account by fliping is active flag

        :param account_guid:
        :return:
        """
        CommonValidator.validate_account_guid(account_guid)
        AccountsAdapter.update({
            'account_guid': account_guid
        }, {
            'is_active': False
        })
