from database import db
from models.nerds import Nerds
from models.users import Users
from dal.base_adapter import BaseAdapter


class NerdAdapter(BaseAdapter):

    def __init__(self):
        BaseAdapter.__init__(self)

    @staticmethod
    def create(account=None,
               nerd_guid=None,
               nerd_name=None,
               nerd_url=None,
               is_deleted=False,
               is_active=True,
               user=None):

        nerd = Nerds(
            nerd_url=nerd_url,
            nerd_guid=nerd_guid,
            nerd_name=nerd_name,
            is_deleted=is_deleted,
            is_active=is_active,
        )
        nerd.users.append(user)
        account.nerds.append(nerd)
        db.add(account)
        db.commit()

    @staticmethod
    def read_by_user(user_id=None, account_id=None):
        bots = db.query(Nerds).filter(Nerds.users.any(user_id=user_id)).\
            filter(Nerds.account_id.like(account_id)).all()
        assert isinstance(bots, list)
        return bots

    @staticmethod
    def read_nerd_by_user_and_nerd_guid(user_id=None, account_id=None, nerd_guid=None):
        bots = db.query(Nerds).filter(Nerds.users.any(user_id=user_id)). \
            filter(Nerds.account_id.like(account_id)). \
            filter(Nerds.nerd_guid.like(nerd_guid)).all()
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
        db.query(Nerds) \
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
        bot = db.query(Nerds). \
            filter_by(**query).one()
        bot.users.append(user)
        db.commit()
