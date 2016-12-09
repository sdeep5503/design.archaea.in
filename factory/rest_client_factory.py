from design_config import MOCK_NERD_RESPONSE
from restclient.nerd_rest_client import NerdRestClient
from tests.mocks.nerd_mock_rest_client import NerdMockRestClient


class NerdRestClientFactory:

    def __init__(self, nerd_base_url):
        self.nerd_base_url = nerd_base_url

    def getNerdRestClient(self, is_mock=False):
        if is_mock or MOCK_NERD_RESPONSE:
            return NerdMockRestClient(self.nerd_base_url)
        return NerdRestClient(self.nerd_base_url)


