from dal.user_adapter import UserAdapter


class UserService:

    def __init__(self):
        pass

    @staticmethod
    def get_user_by_email(email=None):
        """
        Reads Users

        :param email:
        :return:
        """
        return UserAdapter.read({
            'email': email
        })

    @staticmethod
    def get_user_by_guid(user_guid=None):
        """
        Reads Users

        :param user_guid:
        :return:
        """
        return UserAdapter.read({
            'user_guid': user_guid
        })
