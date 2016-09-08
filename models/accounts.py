import datetime
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, Boolean

account_user_association_table = Table('accounts_users', Base.metadata,
                                       Column('account_id', Integer,
                                              ForeignKey('accounts.account_id', ondelete='CASCADE',
                                                         onupdate='CASCADE')),
                                       Column('user_id', Integer,
                                              ForeignKey('users.user_id', ondelete='CASCADE', onupdate='CASCADE')),
                                       Column('permission', String(20), default='member'))


class Accounts(Base):

    __tablename__ = 'accounts'

    account_id = Column(Integer, primary_key=True, nullable=False)
    account_name = Column(String(50), nullable=False)
    account_guid = Column(String(120), unique=True, nullable=False)
    account_type = Column(String(50), nullable=False)
    is_active = Column(Boolean, nullable=False)
    is_deleted = Column(Boolean, nullable=False)
    bots = relationship('Bots', cascade='all, save-update, delete')
    users = relationship('Users', cascade='all, save-update, delete',
                         secondary=account_user_association_table)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow())

    def __init__(self, account_name=None, account_guid=None, account_type=None,
                 is_active=True, is_deleted=False):
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
        self.account_type = account_type
        self.is_active = is_active
        self.is_deleted = is_deleted

    def __repr__(self):
        return '<Accounts %r>' % self.account_name

