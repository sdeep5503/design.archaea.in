from database import db
from models.users import Users
from models.accounts import Accounts
from dal.data_base_adapter import DataBaseAdapter


class AccountsDataAdapter(DataBaseAdapter):

    def __init__(self):
        DataBaseAdapter.__init__(self)

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
        db.query(Accounts). \
            filter_by(**query). \
            delete()
        db.commit()

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



AccountsDataAdapter.add_user()
