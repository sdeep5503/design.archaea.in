from database import db


class DataBaseAdapter:

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
