from database import db
from models.users import Users
from dal.base_adapter import BaseAdapter


class UserAdapter(BaseAdapter):

    def __init__(self):
        BaseAdapter.__init__(self)

    @staticmethod
    def create(user_guid=None,
               email=None,
               password=None,
               first_name=None,
               last_name=None,
               company=None
               ):
        try:
            user = Users(user_guid=user_guid,
                         email=email,
                         password=password,
                         first_name=first_name,
                         last_name=last_name,
                         company=company)
            db.add(user)
            db.commit()
            return user
        except Exception as e:
            db.rollback()
            raise Exception(e.message)

    @staticmethod
    def update(query=None, new_user=None):
        """
        This method update the user

        :param query:
        :param new_user:
        :return:
        """
        try:
            db.query(Users) \
                .filter_by(**query) \
                .update(new_user)
            db.commit()
        except Exception as e:
            db.rollback()
            raise Exception(e.message)

    @staticmethod
    def delete(query=None):
        """
        This methods deletes the record

        :param query:
        :return:
        """
        try:
            db.query(Users).\
                filter_by(**query).\
                delete()
            db.commit()
        except Exception as e:
            db.rollback()
            raise Exception(e.message)

    @staticmethod
    def read(query=None):
        """
        Reading the records from a table

        :param query:
        :return:
        """
        try:
            users = db.query(Users)\
                .filter_by(**query).all()
            assert isinstance(users, list)
            return users
        except Exception as e:
            db.rollback()
            raise Exception(e.message)
