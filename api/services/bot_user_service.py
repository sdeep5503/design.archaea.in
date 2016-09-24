from dal.bot_adapter import BotAdapter


class BotUserService:

    def __init__(self):
        pass

    @staticmethod
    def get_all_bots_with_user_permission(user, account):
        list_of_bots = BotAdapter.read_by_user(user_id=user.user_id,
                                               account_id=account.account_id)
        return list_of_bots
