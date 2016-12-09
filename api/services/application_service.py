from factory.rest_client_factory import NerdRestClientFactory
import json


class ApplicationService:

    def __init__(self):
        pass

    @staticmethod
    def create_application(account_id=None,
                           application_name=None,
                           application_algorithm=None,
                           created_user_id=None,
                           parameters=None,
                           nerd_url=None):
        data = {
            'application_name': application_name,
            'account_id': account_id,
            'algorithm': application_algorithm,
            'user_id': created_user_id,
            'parameters': parameters
        }
        nerd_rest_client = NerdRestClientFactory(nerd_base_url=nerd_url).getNerdRestClient()
        result = nerd_rest_client.create_application(data)
        return result

    @staticmethod
    def get_application(nerd_url):
        nerd_rest_client = NerdRestClientFactory(nerd_base_url=nerd_url).getNerdRestClient()
        result = nerd_rest_client.get_applications()
        return result

    @staticmethod
    def get_application_by_guid(nerd_url, application_guid):
        nerd_rest_client = NerdRestClientFactory(nerd_base_url=nerd_url).getNerdRestClient()
        result = nerd_rest_client.get_application_by_guid(application_guid=application_guid)
        return result