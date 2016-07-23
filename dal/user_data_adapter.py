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
    def update(query=None, new_user=None):
        """
        This method update the user

        :param query:
        :param new_user:
        :return:
        """
        db.query(Users) \
            .filter_by(**query) \
            .update(new_user)
        db.commit()

    @staticmethod
    def delete(query=None):
        """
        This methods deletes the record

        :param query:
        :return:
        """
        db.query(Users).\
            filter_by(**query).\
            delete()
        db.commit()

    @staticmethod
    def read(query=None):
        """
        Reading the records from a table

        :param query:
        :return:
        """
        users = db.query(Users)\
            .filter_by(**query).all()
        assert isinstance(users, list)
        return users


print UserDataAdapter.create(user_guid='my_name',
                     email='is@g',
                     password='khan',
                     first_name='fn',
                     last_name='ln',
                     company='my')
