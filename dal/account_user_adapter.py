from database import engine
from dal.base_adapter import BaseAdapter
from models.accounts import account_user_association_table


class AccountUserAdapter(BaseAdapter):

    def __init__(self):
        BaseAdapter.__init__(self)

    @staticmethod
    def update(query=None, permission=None):
        """
        Updating Account_User Table

        :param permission:
        :param query:
        :return:
        """
        sql_query = account_user_association_table.update().where(
            account_user_association_table.c.account_id == query['account_id']).where(
            account_user_association_table.c.user_id == query['user_id'])\
            .values(permission=permission)
        engine.execute(sql_query)

    @staticmethod
    def read_by_user_id(user_id=None):
        """
        This methods returns all the records with the given user_guid

        :param user_id:
        :return:
        """
        sql_query = account_user_association_table.select().where(
            account_user_association_table.c.user_id == user_id)
        return engine.execute(sql_query).fetchall()

    def read_by_guid(user_guid=None, account_guid=None):
        pass

    @staticmethod
    def read(user_id, account_id):
        sql_query = account_user_association_table.select().where(
            account_user_association_table.c.user_id == user_id).where(
            account_user_association_table.c.account_id == account_id)
        return engine.execute(sql_query).fetchall()