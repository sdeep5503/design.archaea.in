

class CommonValidator:

    def __init__(self):
        pass

    @staticmethod
    def validate_account_guid(account_guid):
        if account_guid or len(account_guid) == 0:
            raise Exception('[Services] Account GUID should contain atleast one character')

    @staticmethod
    def validate_user_guid(user_guid):
        if user_guid or len(user_guid) == 0:
            raise Exception('[Services] User GUID should contain atleast one character')