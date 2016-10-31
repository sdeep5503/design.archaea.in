from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from design_config import APPS_DB_URL

engine = create_engine(APPS_DB_URL, convert_unicode=True)
apps_db = scoped_session(sessionmaker(autocommit=False,
                                 autoflush=False,
                                 bind=engine))

AppDBBase = declarative_base()
AppDBBase.query = apps_db.query_property()


def init_apps_db():
    """
    This method initiates the data base for the first time

    :return:
    """
    import models.dump2
    import models.applications
    import models.application_bots

    AppDBBase.metadata.create_all(bind=engine)


def destroy_session():
    """
    This function destroys the session with db

    :return:
    """
    apps_db.remove()


init_apps_db()
