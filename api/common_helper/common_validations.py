

class CommonValidator:

    def __init__(self):
        pass

    @staticmethod
    def validate_account_guid(account_guid):
        if not account_guid:
            raise Exception('[Services] Invalid Account GUID')

    @staticmethod
    def validate_user_guid(user_guid):
        if not user_guid:
            raise Exception('[Services] Invalid Account GUID')