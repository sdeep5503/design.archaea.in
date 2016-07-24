import datetime
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, Boolean

application_user_association_table = Table('application_user', Base.metadata,
                                           Column('application_id', Integer, ForeignKey('applications.application_id')),
                                           Column('user_id', Integer, ForeignKey('users.user_id'))
                                           )


class Applications(Base):
    __tablename__ = 'applications'

    application_id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.account_id'))
    application_name = Column(String(50))
    application_guid = Column(String(120), unique=True)
    is_deleted = Column(Boolean, nullable=False)
    algorithm_name = Column(String(20), nullable=False)
    linear_regressions = relationship("LinearRegression")

    created = Column(DateTime, default=datetime.datetime.utcnow)
    updated = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, application_guid=None,
                 application_name=None,
                 is_deleted=False,
                 algorithm_name=None):
        """
        Constructor to create a application

        :param application_guid:
        :param application_name:
        :param is_deleted:
        :param algorithm_name:
        """
        self.application_guid = application_guid
        self.application_name = application_name
        self.is_deleted = is_deleted
        self.algorithm_name = algorithm_name

    def __repr__(self):
        return '<Applications %r>' % self.account_name
