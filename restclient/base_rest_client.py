import json
import requests


class BaseRestClient:

    def __init__(self):
        pass

    @staticmethod
    def post(url, headers=None, data=None):
        return requests.post(url=url, data=json.dumps(data), headers=headers)
