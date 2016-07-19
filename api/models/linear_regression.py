import datetime
from api.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class LinearRegression(Base):

    __tablename__ = 'linear_regression'

    algorithm_id = Column(Integer, primary_key=True)
    application_id = Column(Integer, ForeignKey('applications.application_id'))
    algorithm_guid = Column(String(120), unique=True)
    deleted = Column(Integer, nullable=False)

    created= Column(DateTime, default=datetime.datetime.utcnow)
    updated= Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, account_name=None, email=None):
        self.name = account_name
        self.email = email

    def __repr__(self):
        return '<Applications %r>' % self.account_name
