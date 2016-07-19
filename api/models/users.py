import datetime
from api.database import Base
from sqlalchemy import Column, Integer, String, DateTime


class Users(Base):

    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_guid = Column(String(120), unique=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    first_name = Column(String(20))
    last_name = Column(String(20))
    company = Column(String(20))

    created = Column(DateTime, default=datetime.datetime.utcnow)
    updated = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, user_guid=None, email=None):
        self.user_guid = user_guid
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.user_guid
