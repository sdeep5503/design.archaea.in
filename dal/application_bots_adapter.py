from apps_database import apps_db
from models.application_bots import ApplicationBots


class ApplicationBotsAdapter:
    def __init__(self):
        pass

    @staticmethod
    def create(application_id=None,
               bot_id=None):
        app_bot = ApplicationBots(application_id=application_id,
                                  bot_id=bot_id)
        apps_db.add(app_bot)
        apps_db.commit()

    @staticmethod
    def read(query=None):
        """
        Reading the records from a table

        :param query:
        :return:
        """
        apps = apps_db.query(ApplicationBots) \
            .filter_by(**query).all()
        assert isinstance(apps, list)
        return apps