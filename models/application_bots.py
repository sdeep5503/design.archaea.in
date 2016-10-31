import datetime
from apps_database import AppDBBase
from sqlalchemy import Column, Integer, DateTime


class ApplicationBots(AppDBBase):

    __tablename__ = 'application_bots'

    application_id = Column(Integer, nullable=False)
    bot_id = Column(Integer, nullable=False)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow())

    def __init__(self,
                 account_id=None,
                 bot_id=None):

        self.account_id = account_id
        self.bot_id = bot_id

    def __repr__(self):
        return '<ApplicationBots %r>' % self.bot_id

