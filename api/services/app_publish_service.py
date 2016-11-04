from dal.application_bots_adapter import ApplicationBotsAdapter


class ApplicationPublishServices:

    def __init__(self):
        pass

    @staticmethod
    def publish_app(application_id=None,
                    bot_id=None):
        create(application_id=application_id,
                             bot_id=bot_id)