from database import engine
from models.nerds import nerd_user_association_table


class UserNerdAdapter:

    def __init__(self):
        pass

    @staticmethod
    def get_user_nerd_by_user_id_and_nerd_id(user_id=None,
                                             nerd_id=None):
        sql_query = nerd_user_association_table.select().where(
            nerd_user_association_table.c.user_id == user_id).where(
            nerd_user_association_table.c.nerd_id == nerd_id
        )
        return engine.execute(sql_query).fetchall()
