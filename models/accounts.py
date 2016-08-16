import datetime
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, Boolean

account_user_association_table = Table('accounts_users', Base.metadata,
                                       Column('account_guid', String(120),
                                              ForeignKey('accounts.account_guid', ondelete='CASCADE',
                                                         onupdate='CASCADE')),
                                       Column('user_guid', String(120),
                                              ForeignKey('users.user_guid', ondelete='CASCADE', onupdate='CASCADE')),
                                       Column('permission', String(20), default='member'))


class Accounts(Base):
    __tablename__ = 'accounts'

    account_id = Column(Integer, primary_key=True, nullable=False)
    account_name = Column(String(50), nullable=False)
    account_guid = Column(String(120), unique=True, nullable=False)
    is_active = Column(Boolean, nullable=False)
    is_trail = Column(Boolean, nullable=False)
    is_enterprise = Column(Boolean, nullable=False)
    is_deleted = Column(Boolean, nullable=False)
    bots = relationship('Bots', cascade='all, save-update, delete')
    users = relationship('Users', cascade='all, save-update, delete',
                         secondary=account_user_association_table)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, account_name=None, account_guid=None, is_active=True,
                 is_trail=True, is_enterprise=False, is_deleted=False):
        """

        :param account_name:
        :param account_guid:
        :param is_active:
        :param owner_id:
        :param is_trail:
        :param is_enterprise:
        :param is_deleted:
        """
        self.account_name = account_name
        self.account_guid = account_guid
        self.is_active = is_active
        self.is_trail = is_trail
        self.is_enterprise = is_enterprise
        self.is_deleted = is_deleted

    def __repr__(self):
        return '<Accounts %r>' % self.account_name
