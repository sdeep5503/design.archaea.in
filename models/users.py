import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean

from database import Base


class Users(Base):

    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_guid = Column(String(120), unique=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    first_name = Column(String(20))
    last_name = Column(String(20))
    is_system = Column(Boolean, nullable=False)
    company = Column(String(20))

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow())

    def __init__(self, user_guid=None,
                 email=None,
                 password = None,
                 first_name= None,
                 last_name=None,
                 is_system=False,
                 company=None):
        """
        Create User

        :param user_guid:
        :param email:
        :param password:
        :param first_name:
        :param last_name:
        :param company:
        """
        self.user_guid = user_guid
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.is_system = is_system
        self.company = company

    def __repr__(self):
        return '<User %r>' % self.email
