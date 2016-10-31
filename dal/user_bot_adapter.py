from database import engine
from models.bots import bot_user_association_table


class UserBotAdapter:

    def __init__(self):
        pass

    @staticmethod
    def get_user_bot_by_user_id_and_bot_id(user_id=None,
                                           bot_id=None):
        sql_query = bot_user_association_table.select().where(
            bot_user_association_table.c.user_id == user_id).where(
            bot_user_association_table.c.bot_id == bot_id
        )
        return engine.execute(sql_query).fetchall()
