import datetime
from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean


class LinearRegression(Base):

    __tablename__ = 'linear_regression'

    algorithm_id = Column(Integer, primary_key=True)
    application_id = Column(Integer, ForeignKey('applications.application_id'))
    algorithm_guid = Column(String(120), unique=True)
    fit_intercept = Column(Boolean, default=True)
    normalize = Column(Boolean, default=False)
    copy_X = Column(Boolean, default=True)
    n_jobs = Column(Integer, default=1)
    is_deleted = Column(Boolean, nullable=False)

    created_at= Column(DateTime, default=datetime.datetime.utcnow)
    updated_at= Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, algorithm_guid=None,
                       fit_intercept=True,
                       normalize=False,
                       copy_X=True,
                       n_jobs=1):
        """
        Create a Linear regression

        :param algorithm_guid:
        :param fit_intercept:
        :param normalize:
        :param copy_X:
        :param n_jobs:
        """

        self.algorithm_guid = algorithm_guid
        self.fit_intercept = fit_intercept
        self.normalize = normalize
        self.copy_X = copy_X
        self.n_jobs =n_jobs

    def __repr__(self):
        return '<LinearRegression %r>' % self.algorithm_guid
