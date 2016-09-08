from models.bots import Bots
from accounts_adapter import AccountsAdapter


class BotAdapter:

    def __init__(self):
        pass
    
    @staticmethod
    def create_bot(account_guid=None,
                   bot_guid=None,
                   bot_name=None,
                   bot_description=None,
                   is_deleted=False,
                   is_active=False,
                   bot_metadata=None,
                   bot_secret=None,
                   bot_key=None):
        """

        :param account_guid:
        :param bot_guid:
        :param bot_name:
        :param bot_description:
        :param is_deleted:
        :param is_active:
        :param bot_metadata:
        :param bot_secret:
        :param bot_key:
        :return:
        """
        account = AccountsAdapter.read(query={
            'account_guid': account_guid
        })[0]
        if not account:
            raise Exception('[Adapter] The account that you are trying to create the app does not exist')
        account.bots.append(Bots(
            bot_guid=bot_guid,
            bot_name=bot_name,
            bot_description=bot_description,
            is_deleted=is_deleted,
            is_active=is_active,
            bot_metadata=bot_metadata,
            bot_secret=bot_secret,
            bot_key=bot_key
        ))