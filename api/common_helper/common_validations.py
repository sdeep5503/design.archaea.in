from functools import wraps
from common_constants import ApiRequestConstants
from flask import request, make_response, jsonify
from http_constants import HttpExceptions, HttpStatus


class CommonValidator:
    def __init__(self):
        pass

    @staticmethod
    def validate_account_guid(account_guid):
        if not account_guid:
            raise Exception('[Services] Invalid Account GUID')

    @staticmethod
    def validate_user_guid(user_guid):
        if not user_guid:
            raise Exception('[Services] Invalid Account GUID')


class RequestValidator:

    def __init__(self):
        pass

    @staticmethod
    def __request_id_not_found():
        """
        The error thrown in case request Id not found

        :return:
        """
        request_id_failure = {
            'message': HttpExceptions.REQUEST_ID_NOT_FOUND
        }
        return make_response(jsonify(request_id_failure), HttpStatus.PRE_CONDITION_FAILED)

    @staticmethod
    def __wrong_content_type():
        """
        The error thrown in case request Id not found

        :return:
        """
        content_type_failure = {
            'message': HttpExceptions.CONTENT_TYPE_INVALID
        }
        return make_response(jsonify(content_type_failure), HttpStatus.PRE_CONDITION_FAILED)

    @staticmethod
    def validate_request_header(f):
        """
            The decorator for basic auth

            :param f:
            :return:
            """

        @wraps(f)
        def decorated(*args, **kwargs):
            request_id = request.headers.get(ApiRequestConstants.X_REQUEST_ID)
            content_type = request.headers.get('Content-Type')
            if not content_type or not (content_type == 'application/json'):
                return RequestValidator.__wrong_content_type()
            if not request_id:
                return RequestValidator.__request_id_not_found()
            return f(*args, **kwargs)
        return decorated
