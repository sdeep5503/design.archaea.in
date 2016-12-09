import datetime

from sqlalchemy import Column, Integer, String, DateTime

from database import Base


class Dump(Base):

    __tablename__ = 'dummy'

    application_id = Column(Integer, primary_key=True)
    application_name = Column(String(50))
    application_guid = Column(String(120), unique=True)
    active = Column(Integer, default=0)
    owner_id = Column(Integer, nullable=False)
    enterprise = Column(Integer, nullable=False)
    deleted = Column(Integer, nullable=False)

    created= Column(DateTime, default=datetime.datetime.utcnow)
    updated= Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, account_name=None, email=None):
        self.name = account_name
        self.email = email

    def __repr__(self):
        return '<Dump %r>' % self.account_name
