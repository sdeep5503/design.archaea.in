import json
import requests
from design_config import EXTERNAL_REQUEST_TIMEOUT


class BaseRestClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, path, headers=None, data=None):
        url = self.base_url + path
        return requests.post(url=url, data=json.dumps(data), headers=headers, timeout=EXTERNAL_REQUEST_TIMEOUT)

    def get(self, path, headers=None, query_string=None):
        url = self.base_url + path
        if query_string is not None: url += query_string
        return requests.get(url, headers=headers, timeout=EXTERNAL_REQUEST_TIMEOUT)