import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean

from database import Base


class Users(Base):

    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_guid = Column(String(255), unique=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    company = Column(String(255), nullable=False)

    is_system = Column(Boolean, nullable=False, default=False)
    is_active = Column(Boolean, nullable=False, default=False)
    is_deleted = Column(Boolean, nullable=False, default=False)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow())

    def __init__(self, user_guid=None,
                 email=None,
                 password=None,
                 first_name=None,
                 last_name=None,
                 company=None,
                 is_system=None,
                 is_active=False,
                 is_deleted=False):
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
        self.company = company
        self.is_system = is_system
        self.is_active = is_active
        self.is_deleted = is_deleted

    def __repr__(self):
        return '<User %r>' % self.email
