import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean

from database import Base


class LinearRegression(Base):

    __tablename__ = 'linear_regression'

    algorithm_id = Column(Integer, primary_key=True)
    application_id = Column(Integer, ForeignKey('applications.application_id'))
    algorithm_guid = Column(String(120), unique=True)
    fit_intercept = Column(Boolean, default=True)
    normalize = Column(Boolean, default=False)
    copy_X = Column(Boolean, default=True)
    n_jobs = Column(Integer, default=True)
    deleted = Column(Integer, nullable=False)

    created= Column(DateTime, default=datetime.datetime.utcnow)
    updated= Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, account_name=None, email=None):
        self.name = account_name
        self.email = email

    def __repr__(self):
        return '<LinearRegression %r>' % self.account_name
