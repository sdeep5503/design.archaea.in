from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from design_config import DESIGN_DB_URL

engine = create_engine(DESIGN_DB_URL, convert_unicode=True)
db = scoped_session(sessionmaker(autocommit=False,
                                 autoflush=False,
                                 bind=engine))

Base = declarative_base()
Base.query = db.query_property()


def init_db():
    """
    This method initiates the data base for the first time

    :return:
    """
    import models.users
    import models.accounts
    import models.nerds

    Base.metadata.create_all(bind=engine)


def destroy_session():
    """
    This function destroys the session with db

    :return:
    """
    db.remove()
