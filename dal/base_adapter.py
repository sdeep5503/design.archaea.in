from database import db


class BaseAdapter:

    def __init__(self):
        pass

    @staticmethod
    def get_db_session():
        """
        Get db session object

        :return:
        """
        return db

    @staticmethod
    def destroy_db_session():
        """
        Remove DB session

        :return:
        """
        db.remove()

    @staticmethod
    def create():
        pass

    @staticmethod
    def update():
        pass

    @staticmethod
    def delete():
        pass
