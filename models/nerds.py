import datetime
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, Boolean

nerd_user_association_table = Table('nerd_users', Base.metadata,
                                    Column('nerd_id', Integer,
                                           ForeignKey('nerds.nerd_id', ondelete='CASCADE', onupdate='CASCADE')),
                                    Column('user_id', Integer,
                                           ForeignKey('users.user_id', ondelete='CASCADE', onupdate='CASCADE')))


class Nerds(Base):

    __tablename__ = 'nerds'

    nerd_id = Column(Integer, primary_key=True)
    nerd_guid = Column(String(45), unique=True)
    account_id = Column(Integer, ForeignKey('accounts.account_id', ondelete='CASCADE',
                                            onupdate='CASCADE'))
    users = relationship('Users', cascade='all, save-update, delete',
                         secondary=nerd_user_association_table)
    nerd_name = Column(String(255), nullable=False)
    nerd_url = Column(String(2083), nullable=False)
    is_deleted = Column(Boolean, nullable=False, default=False)
    is_active = Column(Boolean, nullable=False, default=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow())

    def __init__(self, nerd_guid=None,
                 nerd_name=None,
                 is_deleted=False,
                 is_active=False,
                 nerd_url=None):
        self.nerd_guid = nerd_guid
        self.nerd_name = nerd_name
        self.nerd_url = nerd_url
        self.is_active = is_active
        self.is_deleted = is_deleted

    def __repr__(self):
        return '<Nerds %r>' % self.nerd_name
