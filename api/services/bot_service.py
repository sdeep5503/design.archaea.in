from models.users import Users
from dal.bot_adapter import BotAdapter


class BotService:
    def __init__(self):
        pass

    @staticmethod
    def create_bot(account_guid=None,
                   bot_guid=None,
                   bot_name=None,
                   bot_description=None,
                   is_deleted=False,
                   is_active=True,
                   bot_metadata=None,
                   bot_secret=None,
                   bot_key=None,
                   user=None):
        if not isinstance(user, Users):
            raise Exception('[Services] User not found while creating bot')
        BotAdapter.create(account_guid=account_guid,
                          bot_guid=bot_guid,
                          bot_name=bot_name,
                          bot_description=bot_description,
                          is_deleted=is_deleted,
                          is_active=is_active,
                          bot_metadata=bot_metadata,
                          bot_secret=bot_secret,
                          bot_key=bot_key,
                          user=user)
        # TODO This method should return the app key, secret and guid
