import uuid


class CommonHelper:

    def __init__(self):
        pass

    @staticmethod
    def generate_guid():
        return str(uuid.uuid1())
