from dal.application_adapter import ApplicationsAdapter
from api.common_helper.common_utils import CommonHelper
from dal.application_bots_adapter import ApplicationBotsAdapter


class ApplicationsService:

    def __init__(self):
        pass

    @staticmethod
    def create_application(account_id=None,
                           application_name=None,
                           application_algorithm=None,
                           user_id=None,
                           app_metadata=None,
                           bot_id=None):
        application_key = CommonHelper.generate_guid()
        application_secret = CommonHelper.generate_guid()
        app_details = ApplicationsAdapter.create(account_id=account_id,
                                                 application_name=application_name,
                                                 application_guid=CommonHelper.generate_guid(),
                                                 application_key=application_key,
                                                 application_secret=application_secret,
                                                 application_algorithm=application_algorithm,
                                                 user_id=user_id,
                                                 app_metadata=app_metadata)
        ApplicationBotsAdapter.create(account_id=account_id, bot_id=bot_id)
        return app_details
