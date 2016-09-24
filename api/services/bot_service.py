from models.users import Users
from dal.bot_adapter import BotAdapter
from api.common_helper.common_utils import CommonHelper
from api.services.account_user_service import AccountUserService


class BotService:

    def __init__(self):
        pass

    @staticmethod
    def create_bot(account=None,
                   bot_name=None,
                   is_deleted=False,
                   is_active=True,
                   bot_metadata=None,
                   user=None):
        if not isinstance(user, Users):
            raise Exception('[Services] User not found while creating bot')
        bot_guid = CommonHelper.generate_guid()
        BotAdapter.create(account=account,
                          bot_guid=bot_guid,
                          bot_name=bot_name,
                          is_deleted=is_deleted,
                          is_active=is_active,
                          bot_metadata=bot_metadata,
                          user=user)

    @staticmethod
    def read(account=None, user=None):
        account_permission = AccountUserService.get_permission(user=user,account=account)
        if not account_permission:
            return []
        return BotAdapter.read_by_user(
            user_id=user.user_id,
            account_id=account.account_id
        )