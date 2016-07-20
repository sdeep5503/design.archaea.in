from database import db
from models.users import Users
from dal.data_base_adapter import DataBaseAdapter


class UserDataAdapter(DataBaseAdapter):
    def __init__(self):
        DataBaseAdapter.__init__(self)

    @staticmethod
    def create(user_guid=None,
               email=None,
               password=None,
               first_name=None,
               last_name=None,
               company=None
               ):
        """
        This method does the database call to create a user

        :param user_guid:
        :param email:
        :param password:
        :param first_name:
        :param last_name:
        :param company:
        :return:
        """
        user = Users(user_guid=user_guid,
                     email=email,
                     password=password,
                     first_name=first_name,
                     last_name=last_name,
                     company=company)
        db.add(user)
        db.commit()

    @staticmethod
    def update(user_guid, new_user):
        """
        This method update the user

        :param user_guid:
        :param new_user:
        :return:
        """
        db.query(Users)\
            .filter_by(user_guid=user_guid)\
            .update(new_user)
        db.commit()
        


UserDataAdapter.update(user_guid='ecbkdnck',
                       new_user={'email':u'satic.vishnu.vinu', 'password':u'kabali'})