from api.common_helper.common_constants import NerdUrlPaths
from restclient.base_rest_client import BaseRestClient
from api.common_helper.common_constants import ApiRequestConstants


class NerdRestClient(BaseRestClient):

    def __init__(self, nerd_base_url):
        BaseRestClient.__init__(self, nerd_base_url)
        self.headers = {
            ApiRequestConstants.CONTENT_TYPE: 'application/json'
        }

    def create_application(self, application_object):
        result = self.post(path=NerdUrlPaths.NERD_APPLICATION_PATH, data=application_object, headers=self.headers)
        return result

    def get_applications(self, query_params=None):
        return self.get(path=NerdUrlPaths.NERD_APPLICATION_PATH, headers=self.headers, query_string=query_params)

    def get_application_by_guid(self, query_params=None, application_guid=None):
        return self.get(path=NerdUrlPaths.NERD_APPLICATION_PATH + '/' + application_guid,
                        headers=self.headers, query_string=query_params)
