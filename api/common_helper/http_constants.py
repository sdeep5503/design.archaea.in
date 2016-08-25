class HttpExceptions:

    REQUEST_ID_NOT_FOUND = '[Invalid Param] X-Request-id not found'
    CONTENT_TYPE_INVALID = '[Invalid Param] content type not valid'

    def __init__(self):
        pass


class HttpStatus:

    OK = 200
    UNAUTHORIZED = 401,
    PRE_CONDITION_FAILED = 412

    def __init__(self):
        pass
