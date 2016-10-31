from dal.bot_adapter import BotAdapter
from dal.user_bot_adapter import UserBotAdapter


class BotUserService:

    def __init__(self):
        pass

    @staticmethod
    def get_all_bots_with_user_permission(user, account):
        list_of_bots = BotAdapter.read_by_user(user_id=user.user_id,
                                               account_id=account.account_id)
        return list_of_bots

    @staticmethod
    def has_user_permission_on_bot(user=None, bot=None):
        UserBotAdapter.get_user_bot_by_user_id_and_bot_id(user_id=user.user_id,
                                                          bot_id=bot.bot_id)
