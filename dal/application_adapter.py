from apps_database import apps_db
from base_adapter import BaseAdapter
from models.applications import Applications


class ApplicationsAdapter(BaseAdapter):
    def __init__(self):
        BaseAdapter.__init__(self)

    @staticmethod
    def create(account_id=None,
               application_name=None,
               application_algorithm=None,
               user_id=None,
               app_metadata=None,
               application_key=None,
               application_secret=None,
               application_guid=None):
        application = Applications(account_id=account_id,
                                   application_name=application_name,
                                   application_guid=application_guid,
                                   application_key=application_key,
                                   application_secret=application_secret,
                                   application_algorithm=application_algorithm,
                                   user_id=user_id,
                                   app_metadata=app_metadata)
        apps_db.add(application)
        apps_db.commit()
        return {
            'application_id': application.application_id,
            'application_key': application.application_key,
            'application_secret': application.application_secret
        }


    @staticmethod
    def update(query=None, updated_value=None):
        """
        This method update the account

        :param query:
        :param updated_value:
        :return:
        """
        apps_db.query(Applications) \
            .filter_by(**query) \
            .update(updated_value)
        apps_db.commit()

    @staticmethod
    def delete(query=None):
        """
        This methods deletes the record

        :param query:
        :return:
        """
        raise Exception('Hard delete on Applications Table is not implemented')

    @staticmethod
    def read(query=None):
        """
        Reading the records from a table

        :param query:
        :return:
        """
        apps = apps_db.query(Applications) \
            .filter_by(**query).all()
        assert isinstance(apps, list)
        return apps

