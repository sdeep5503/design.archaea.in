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

        try:
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
        except Exception as e:
            db.rollback()
            raise Exception(e.message)

    @staticmethod
    def read_by_account(account_id):
        try:
            nerds = db.query(Nerds).filter(Nerds.account_id.like(account_id)).all()
            return nerds
        except Exception as e:
            db.rollback()
            raise Exception(e.message)

    @staticmethod
    def read_by_user(user_id=None, account_id=None):
        try:
            nerds = db.query(Nerds).filter(Nerds.users.any(user_id=user_id)). \
                filter(Nerds.account_id.like(account_id)).all()
            return nerds
        except Exception as e:
            db.rollback()
            raise Exception(e.message)

    @staticmethod
    def read_nerd_by_user_and_nerd_guid(user_id=None, account_id=None, nerd_guid=None):
        try:
            nerds = db.query(Nerds).filter(Nerds.users.any(user_id=user_id)). \
                filter(Nerds.account_id.like(account_id)). \
                filter(Nerds.nerd_guid.like(nerd_guid)).all()
            return nerds
        except Exception as e:
            db.rollback()
            raise Exception(e.message)

    @staticmethod
    def update(query=None, updated_value=None):
        """
        This method update the account

        :param query:
        :param updated_value:
        :return:
        """
        try:
            db.query(Nerds) \
                .filter_by(**query) \
                .update(updated_value)
            db.commit()
        except Exception as e:
            db.rollback()
            raise Exception(e.message)

    @staticmethod
    def add_user(query, user):
        """
        Adds users to an existing account

        :param query:
        :param user:
        :return:
        """
        try:
            nerd = db.query(Nerds). \
                filter_by(**query).one()
            nerd.users.append(user)
            db.commit()
        except Exception as e:
            db.rollback()
            raise Exception(e.message)
