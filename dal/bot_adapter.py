from database import db
from models.bots import Bots
from models.users import Users
from dal.base_adapter import BaseAdapter
from accounts_adapter import AccountsAdapter


class BotAdapter(BaseAdapter):

    def __init__(self):
        BaseAdapter.__init__(self)
    
    @staticmethod
    def create(account_guid=None,
               bot_guid=None,
               bot_name=None,
               bot_description=None,
               is_deleted=False,
               is_active=True,
               bot_metadata=None,
               bot_secret=None,
               bot_key=None,
               user=None):
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
        bot = Bots(
            bot_guid=bot_guid,
            bot_name=bot_name,
            bot_description=bot_description,
            is_deleted=is_deleted,
            is_active=is_active,
            bot_metadata=bot_metadata,
            bot_secret=bot_secret,
            bot_key=bot_key
        )
        bot.users.append(user)
        account.bots.append(bot)
        db.add(account)
        db.commit()

    @staticmethod
    def read(query=None):
        """
        Reading the records from a table

        :param query:
        :return:
        """
        bots = db.query(Bots) \
            .filter_by(**query).all()
        assert isinstance(bots, list)
        return bots

    @staticmethod
    def update(query=None, updated_value=None):
        """
        This method update the account

        :param query:
        :param updated_value:
        :return:
        """
        db.query(Bots) \
            .filter_by(**query) \
            .update(updated_value)
        db.commit()

    @staticmethod
    def add_user(query, user):
        """
        Adds users to an existing account

        :param query:
        :param user:
        :return:
        """
        assert isinstance(user, Users)
        bot = db.query(Bots). \
            filter_by(**query).one()
        bot.users.append(user)
        db.commit()