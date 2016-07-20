import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from database import Base

application_user_association_table = Table('application_user', Base.metadata,
                                           Column('application_id', Integer, ForeignKey('applications.application_id')),
                                           Column('user_id', Integer, ForeignKey('users.user_id'))
                                           )


class Applications(Base):

    __tablename__ = 'applications'

    application_id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.account_id'))
    application_name = Column(String(50))
    application_guid = Column(String(120), unique=True)
    deleted = Column(Integer, nullable=False)
    algorithm = Column(String(20), nullable=False)
    linear_regressions = relationship("LinearRegression")

    created = Column(DateTime, default=datetime.datetime.utcnow)
    updated = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, account_name=None, email=None):
        self.name = account_name
        self.email = email

    def __repr__(self):
        return '<Applications %r>' % self.account_name
