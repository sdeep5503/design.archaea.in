import datetime
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, Boolean

bot_user_association_table = Table('bots_users', Base.metadata,
                                   Column('bot_id', Integer,
                                          ForeignKey('bots.bot_id', ondelete='CASCADE', onupdate='CASCADE')),
                                   Column('user_id', Integer,
                                          ForeignKey('users.user_id', ondelete='CASCADE', onupdate='CASCADE')))


class Bots(Base):
    __tablename__ = 'bots'

    bot_id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.account_id', ondelete='CASCADE',
                                            onupdate='CASCADE'))
    users = relationship('Users', cascade='all, save-update, delete',
                         secondary=bot_user_association_table)
    bot_guid = Column(String(128), unique=True)
    bot_name = Column(String(64))
    is_deleted = Column(Boolean, nullable=False, default=False)
    is_active = Column(Boolean, nullable=False, default=True)
    bot_metadata = Column(String(512), nullable=False)

    created = Column(DateTime, default=datetime.datetime.utcnow)
    updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow())

    def __init__(self, bot_guid=None,
                 bot_name=None,
                 is_deleted=False,
                 is_active=False,
                 bot_metadata=None):
        """
        Constructor to create a application

        :param bot_guid:
        :param bot_name:
        :param bot_type:
        :param is_deleted:
        :param bot_metadata:
        """
        self.bot_guid = bot_guid
        self.bot_name = bot_name
        self.is_active = is_active
        self.is_deleted = is_deleted
        self.bot_metadata = bot_metadata

    def __repr__(self):
        return '<Bots %r>' % self.bot_name
