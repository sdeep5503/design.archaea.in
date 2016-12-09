from dal.nerd_adapter import NerdAdapter
from dal.user_nerd_adapter import UserNerdAdapter


class NerdUserService:

    def __init__(self):
        pass

    @staticmethod
    def get_all_nerds_with_user_permission(user, account):
        list_of_bots = NerdAdapter.read_by_user(user_id=user.user_id,
                                               account_id=account.account_id)
        return list_of_bots

    @staticmethod
    def has_user_permission_on_nerd(user=None, nerd=None):
        UserNerdAdapter.get_user_nerd_by_user_id_and_nerd_id(user_id=user.user_id,
                                                          nerd_id=nerd.nerd_id)
