from database import db
from dal.base_adapter import BaseAdapter
from models.applications import Applications
from dal.accounts_adapter import AccountsAdapter
from models.linear_regression import LinearRegression


class ApplicationsAdapter(BaseAdapter):
    def __init__(self):
        BaseAdapter.__init__(self)

    @staticmethod
    def create(application_guid=None,
               application_name=None,
               is_deleted=False,
               account_guid=None):
        """
        Creating a application

        :param account_guid:
        :param application_guid:
        :param application_name:
        :param is_deleted:
        :return:
        """
        application = Applications(application_guid=application_guid,
                                   application_name=application_name,
                                   is_deleted=is_deleted)
        AccountsAdapter.add_application({'account_guid': account_guid}, application)

    @staticmethod
    def update(query=None, new_user=None):
        """
        This method update the user

        :param query:
        :param new_user:
        :return:
        """
        db.query(Applications) \
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
        db.query(Applications). \
            filter_by(**query). \
            delete()
        db.commit()

    @staticmethod
    def read(query=None):
        """
        Reading the records from a table

        :param query:
        :return:
        """
        users = db.query(Applications) \
            .filter_by(**query).all()
        assert isinstance(users, list)
        return users

    @staticmethod
    def add_linear_regression(query, linear_regression):
        """
        Adding linear regression

        :param query:
        :param linear_regression:
        :return:
        """
        assert isinstance(linear_regression, LinearRegression)
        application = db.query(Applications). \
            filter_by(**query).one()
        application.algorithm_name = 'linear_regression'
        application.linear_regressions.append(linear_regression)
        db.commit()
