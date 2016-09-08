from database import db
from models.users import Users
from models.accounts import Accounts
from dal.base_adapter import BaseAdapter
from models.bots import Bots


class AccountsAdapter(BaseAdapter):

    def __init__(self):
        BaseAdapter.__init__(self)

    @staticmethod
    def create(account_name=None,
               account_guid=None,
               account_type=None,
               is_active=True,
               is_deleted=False,
               owner=None):
        """
        Create a Account

        :param account_type:
        :param owner:
        :param account_name:
        :param account_guid:
        :param is_active:
        :param is_deleted:
        :return:
        """
        account = Accounts(account_name=account_name,
                           account_guid=account_guid,
                           account_type=account_type,
                           is_active=is_active,
                           is_deleted=is_deleted)
        if owner:
            account.users.append(owner)
        db.add(account)
        db.commit()
        return account.account_id

    @staticmethod
    def update(query=None, updated_value=None):
        """
        This method update the account

        :param query:
        :param updated_value:
        :return:
        """
        db.query(Accounts) \
            .filter_by(**query) \
            .update(updated_value)
        db.commit()

    @staticmethod
    def delete(query=None):
        """
        This methods deletes the record

        :param query:
        :return:
        """
        raise Exception('Hard delete on Accounts Table not implemented')

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
    def add_bot(query, bot):
        """
        Adding applications to accounts

        :param query:
        :param bot:
        :return:
        """
        assert isinstance(bot, Bots)
        account = db.query(Accounts). \
            filter_by(**query).one()
        account.bots.append(bot)
        db.commit()

    @staticmethod
    def read_accounts_by_id_list(id_list=None):
        """
        Reading the records from a table

        :param query:
        :return:
        """
        accounts = db.query(Accounts) \
            .filter(Accounts.account_id.in_(id_list)).all()
        assert isinstance(accounts, list)
        return accounts

AccountsAdapter.update(query={
    'account_id': 1
}, updated_value={
    'account_name': 'vizsat'
})