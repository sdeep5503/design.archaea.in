import datetime
from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, Boolean

application_user_association_table = Table('bots_users', Base.metadata,
                                           Column('bot_id', Integer, ForeignKey('bots.bot_id')),
                                           Column('user_id', Integer, ForeignKey('users.user_id'))
                                           )


class Bots(Base):

    __tablename__ = 'bots'

    bot_id = Column(Integer, primary_key=True)
    bot_guid = Column(String(120), unique=True)
    bot_name = Column(String(50))
    account_id = Column(Integer, ForeignKey('accounts.account_id'))
    bot_type = Column(String(20), nullable=False)
    is_deleted = Column(Boolean, nullable=False)
    bot_metadata = Column(String(20), nullable=False)

    created = Column(DateTime, default=datetime.datetime.utcnow)
    updated = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, bot_guid=None,
                 bot_name=None,
                 bot_type=None,
                 is_deleted=False,
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
        self.bot_type = bot_type
        self.is_deleted = is_deleted
        self.bot_metadata = bot_metadata

    def __repr__(self):
        return '<Bots %r>' % self.bot_name
