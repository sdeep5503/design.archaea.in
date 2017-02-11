from models.users import Users
from dal.nerd_adapter import NerdAdapter
from api.common_helper.common_utils import CommonHelper


class NerdService:
    def __init__(self):
        pass

    @staticmethod
    def create_nerd(account=None,
                    nerd_name=None,
                    nerd_url=None,
                    is_deleted=False,
                    is_active=True,
                    user=None):
        if not isinstance(user, Users):
            raise Exception('[Services] User not found while creating bot')
        nerd_guid = CommonHelper.generate_guid()
        NerdAdapter.create(account=account,
                           nerd_guid=nerd_guid,
                           nerd_name=nerd_name,
                           nerd_url=nerd_url,
                           is_deleted=is_deleted,
                           is_active=is_active,
                           user=user)

    @staticmethod
    def give_permission_to_nerds_by_account(user=None, account=None):
        all_nerds = NerdService.read_by_account(account=account)
        for nerd in all_nerds:
            NerdAdapter.add_user(query={
                'nerd_id': nerd.nerd_id
            }, user=user)

    @staticmethod
    def read(account=None, user=None):
        return NerdAdapter.read_by_user(
            user_id=user.user_id,
            account_id=account.account_id
        )

    @staticmethod
    def read_by_account(account=None):
        return NerdAdapter.read_by_account(
            account_id=account.account_id
        )

    @staticmethod
    def get_nerd_guid(account=None, user=None, nerd_guid=None):
        return NerdAdapter.read_nerd_by_user_and_nerd_guid(
            account_id=account.account_id,
            user_id=user.user_id,
            nerd_guid=nerd_guid)
