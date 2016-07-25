from models.users import Users
from dal.user_adapter import UserAdapter
from dal.accounts_adapter import AccountsAdapter
from api.common_helper.common_utils import CommonHelper


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
            # TODO make this user owner but using AccountUserService
        else:
            raise Exception('[Services] User cannot create multiple accounts. '
                            'Please add yourself to any other account if needed')
        return new_account_guid

    @staticmethod
    def deactivate_account(account_guid=None):
        if account_guid or len(account_guid) == 0:
            raise Exception('[Services] Account GUID should contain atleast one character')
        AccountsAdapter.update({
            'account_guid': account_guid
        },{
            'is_active': False
        })

class AccountUserService:

    def __init__(self):
        pass

    @staticmethod
    def account_user_permission(account_guid=None,
                                user_guid=None,
                                permission=None):
        pass

