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
        print query['account_guid'] + query['user_guid']
        sql_query = account_user_association_table.update().where(
            account_user_association_table.c.account_guid == query['account_guid']).where(
            account_user_association_table.c.user_guid == query['user_guid'])\
            .values(permission=permission)
        engine.execute(sql_query)
