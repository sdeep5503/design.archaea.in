from sqlalchemy import create_engine
from design_config import MY_SQL_HOST_URL
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(MY_SQL_HOST_URL, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    """
    This method initiates the data base for the first time

    :return:
    """


    import api.models.dump
    import api.models.accounts
    import api.models.users
    import api.models.applications
    import api.models.linear_regression
    Base.metadata.create_all(bind=engine)


init_db()
