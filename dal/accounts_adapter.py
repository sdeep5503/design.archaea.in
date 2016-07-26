from log_helper import logger
from database import db
from models.users import Users
from models.accounts import Accounts
from dal.base_adapter import BaseAdapter
from models.applications import Applications


class AccountsAdapter(BaseAdapter):
    def __init__(self):
        BaseAdapter.__init__(self)

    @staticmethod
    def create(account_name=None,
               account_guid=None,
               is_active=None,
               is_trail=None,
               is_enterprise=None,
               is_deleted=None,
               owner=None):
        """
        Create a Account

        :param owner:
        :param account_name:
        :param account_guid:
        :param is_active:
        :param is_trail:
        :param is_enterprise:
        :param is_deleted:
        :return:
        """
        account = Accounts(account_name=account_name,
                           account_guid=account_guid,
                           is_active=is_active,
                           is_trail=is_trail,
                           is_enterprise=is_enterprise,
                           is_deleted=is_deleted)
        if owner:
            account.users.append(owner)
        db.add(account)
        db.commit()

    @staticmethod
    def update(query=None, new_user=None):
        """
        This method update the account

        :param query:
        :param new_user:
        :return:
        """
        db.query(Accounts) \
            .filter_by(**query) \
            .update(new_user)
        db.commit()

    @staticmethod
    def delete(query=None):
        """
        This methods deletes the record

        :param query:
        :return:
        """
        logger.warn('Hard delete on Accounts Table not implemented')

    @staticmethod
    def read(query=None):
        """
        Reading the records from a table

        :param query:
        :return:
        """
        accounts = db.query(Accounts) \
            .filter_by(**query).all()
        assert isinstance(accounts, list)
        return accounts

    @staticmethod
    def add_user(query, user):
        """
        Adds users to an existing account

        :param query:
        :param user:
        :return:
        """
        assert isinstance(user, Users)
        account = db.query(Accounts). \
            filter_by(**query).one()
        account.users.append(user)
        db.commit()

    @staticmethod
    def add_application(query, application):
        """
        Adding applications to accounts

        :param query:
        :param application:
        :return:
        """
        assert isinstance(application, Applications)
        account = db.query(Accounts). \
            filter_by(**query).one()
        account.applications.append(application)
        db.commit()

    @staticmethod
    def read_accounts_by_guids(guid_list=None):
        """
        Reading the records from a table

        :param query:
        :return:
        """
        accounts = db.query(Accounts) \
            .filter(Accounts.account_guid.in_(guid_list)).all()
        assert isinstance(accounts, list)
        return accounts
