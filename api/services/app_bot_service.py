from dal.application_bots_adapter import ApplicationBotsAdapter


class AppBotService:

    def __init__(self):
        pass

    @staticmethod
    def is_app_published_on_bot(bot_id=None,
                                application_id=None):
        app_bot = ApplicationBotsAdapter.read({
            'bot_id': bot_id,
            'application_id': application_id
        })
        if len(app_bot) == 0:
            return False
        return True

