
class NerdMockRestClient:

    def __init__(self, nerd_base_url):
        self.nerd_base_url = nerd_base_url

    def create_application(self, application_object):
        result = {}


