class AccountPermissions:
    # permission names
    OWNER = 'owner'
    MEMBER = 'member'

    def __init__(self):
        pass


class AccountTypes:
    # Types of accounts
    COMMON_NICHE = 'common_niche'
    ENTERPRISE = 'enterprise'
    MARKETPLACE = 'marketplace'

    def __init__(self):
        pass


class ApiVersions:
    def __init__(self):
        pass

    # APi Versions
    API_VERSION_V1 = '/api/v1_0'


class ApiRequestConstants:
    def __init__(self):
        pass

    # Request Keys
    CONTENT_TYPE = 'Content-Type'
    X_REQUEST_ID = 'X-Request-Id'
    X_ARCHAEA_AUTHORIZATION = 'X-Archaea-Authorization'


class NerdUrlPaths:
    def __init__(self):
        pass

    VERSION = '/api/v1_0'
    NERD_APPLICATION_PATH = VERSION + '/applications'
