from api.common_helper.common_constants import NerdUrlPaths
from restclient.base_rest_client import BaseRestClient


class NerdRestClient(BaseRestClient):

    def __init__(self, nerd_base_url):
        BaseRestClient.__init__(self)
        self.nerd_base_url = nerd_base_url

    def create_application(self, application_object):
        applications_url = self.nerd_base_url + NerdUrlPaths
        BaseRestClient.post(applications_url, )
