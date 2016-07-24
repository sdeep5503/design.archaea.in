from database import db
from dal.base_adapter import BaseAdapter
from models.linear_regression import LinearRegression
from dal.applications_adapter import ApplicationsAdapter


class LinearRegressionAdapter(BaseAdapter):
    
    def __init__(self):
        BaseAdapter.__init__(self)

    @staticmethod
    def create(algorithm_guid=None,
               fit_intercept=True,
               normalize=False,
               copy_X=True,
               n_jobs=1,
               application_guid=None):
        linear_regression = LinearRegression(algorithm_guid=algorithm_guid,
                                             fit_intercept=fit_intercept,
                                             normalize=normalize,
                                             copy_X=copy_X,
                                             n_jobs=n_jobs)
        ApplicationsAdapter.add_linear_regression({'application_guid': application_guid}, linear_regression)

    @staticmethod
    def update(query=None, new_user=None):
        """
        This method update the user

        :param query:
        :param new_user:
        :return:
        """
        db.query(LinearRegression) \
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
        db.query(LinearRegression). \
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
        users = db.query(LinearRegression) \
            .filter_by(**query).all()
        assert isinstance(users, list)
        return users
