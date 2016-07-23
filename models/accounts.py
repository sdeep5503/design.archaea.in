import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship

from database import Base

account_user_association_table = Table('account_user', Base.metadata,
                                       Column('account_id', Integer, ForeignKey('accounts.account_id')),
                                       Column('user_id', Integer, ForeignKey('users.user_id')),
                                       Column('permissions', String(20), default='member')
                                       )


class Accounts(Base):

    __tablename__ = 'accounts'

    account_id = Column(Integer, primary_key=True, nullable=False)
    account_name = Column(String(50), nullable=False)
    account_guid = Column(String(120), unique=True, nullable=False)
    is_active = Column(Boolean, nullable=False)
    is_trail =  Column(Boolean, nullable=False)
    is_enterprise = Column(Boolean, nullable=False)
    is_deleted = Column(Boolean, nullable=False)
    applications = relationship("Applications", backref='accounts', lazy='dynamic')
    users = relationship("Users",
                         secondary=account_user_association_table)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, account_name=None, account_guid=None, is_active=True, owner_id=None,
                 is_trail=True, is_enterprise=False, is_deleted = False):
        self.account_name = account_name
        self.account_guid = account_guid
        self.is_active = is_active
        self.is_trail = is_trail
        self.is_enterprise = is_enterprise
        self.is_deleted = is_deleted


    def __repr__(self):
        return '<Accounts %r>' % self.account_name
