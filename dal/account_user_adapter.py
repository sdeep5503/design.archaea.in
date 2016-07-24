from dal.base_adapter import BaseAdapter
from database import db, engine
from models.accounts import account_user_association_table


class AccountUserAdapter(BaseAdapter):
    def __init__(self):
        BaseAdapter.__init__(self)

    @staticmethod
    def update(query=None, new_user=None):
        """
            This method update the user

            :param query:
            :param new_user:
            :return:
            """
        db.query(account_user_association_table) \
            .filter_by(**query) \
            .update(new_user)
        db.commit()


q = account_user_association_table.update().where(account_user_association_table.c.account_guid == '123-123-432-123').where(
                                              account_user_association_table.c.user_guid == '321-233-222-33').values(permission='owner')

engine.execute(q)
