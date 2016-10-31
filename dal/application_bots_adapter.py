from apps_database import apps_db
from models.application_bots import ApplicationBots


class ApplicationBotsAdapter:
    def __init__(self):
        pass

    @staticmethod
    def create(account_id=None,
               bot_id=None):
        app_bot = ApplicationBots(account_id=account_id,
                                  bot_id=bot_id)
        apps_db.add(app_bot)
        apps_db.commit()