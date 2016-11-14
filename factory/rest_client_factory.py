from restclient.nerd_rest_client import NerdRestClient
from restclient.nerd_mock_rest_client import NerdMockRestClient


class NerdRestClientFactory:

    def __init__(self, nerd_base_url):
        self.nerd_base_url = nerd_base_url

    def getNerdRestClient(self, is_mock=False):
        if is_mock:
            return NerdMockRestClient()
        return NerdRestClient()


