from database import db
from models.bots import Bots
from models.users import Users
from dal.base_adapter import BaseAdapter
from models.bots import bot_user_association_table


class BotAdapter(BaseAdapter):
    def __init__(self):
        BaseAdapter.__init__(self)

    @staticmethod
    def create(account=None,
               bot_guid=None,
               bot_name=None,
               is_deleted=False,
               is_active=True,
               bot_metadata=None,
               user=None):
        """

        :param account:
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
        bot = Bots(
            bot_guid=bot_guid,
            bot_name=bot_name,
            is_deleted=is_deleted,
            is_active=is_active,
            bot_metadata=bot_metadata
        )
        bot.users.append(user)
        account.bots.append(bot)
        db.add(account)
        db.commit()

    @staticmethod
    def read_by_user(user_id=None, account_id=None):
        bots = db.query(Bots).filter(Bots.users.any(user_id=user_id)).\
            filter(Bots.account_id.like(account_id)).all()
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
