import datetime
from api.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class Applications(Base):

    __tablename__ = 'applications'

    application_id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.account_id'))
    application_name = Column(String(50))
    application_guid = Column(String(120), unique=True)
    deleted = Column(Integer, nullable=False)
    algorithm = Column(String(20), nullable=False)
    linear_regressions = relationship("LinearRegression")

    created= Column(DateTime, default=datetime.datetime.utcnow)
    updated= Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, account_name=None, email=None):
        self.name = account_name
        self.email = email

    def __repr__(self):
        return '<Applications %r>' % self.account_name
