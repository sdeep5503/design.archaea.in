from base_adapter import BaseAdapter


class ApplicationsAdapter(BaseAdapter):
    def __init__(self):
        BaseAdapter.__init__(self)


def create(account_id=None,
           application_name=None,
           application_algorithm=None,
           user_id=None,
           app_metadata=None,
           application_key=None,
           application_secret=None,
           application_guid=None,
           nerd_guid=None,
           isMock=False):
    if not isMock:
          pass
    else:
        return None
    return {

    }
