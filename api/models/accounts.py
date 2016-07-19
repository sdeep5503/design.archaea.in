import datetime
from api.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table

account_user_association_table = Table('account_user', Base.metadata,
                                       Column('account_id', Integer, ForeignKey('accounts.account_id')),
                                       Column('user_id', Integer, ForeignKey('users.user_id'))
                                       )


class Accounts(Base):

    __tablename__ = 'accounts'

    account_id = Column(Integer, primary_key=True)
    account_name = Column(String(50))
    account_guid = Column(String(120), unique=True)
    active = Column(Integer, default=0)
    owner_id = Column(Integer, nullable=False)
    enterprise = Column(Integer, nullable=False)
    deleted = Column(Integer, nullable=False)
    applications = relationship("Applications")
    users = relationship("Users",
                         secondary=account_user_association_table)

    created = Column(DateTime, default=datetime.datetime.utcnow)
    updated = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, account_name=None, email=None):
        self.name = account_name
        self.email = email

    def __repr__(self):
        return '<Accounts %r>' % self.account_name
