from flask import jsonify, make_response


class HttpResponse:

    def __init__(self):
        pass

    @staticmethod
    def internal_server_error(message):
        response = jsonify({
            'message': message
        })
        return make_response(response, 500)

    @staticmethod
    def accepted(message):
        response = jsonify({
            'message': message
        })
        return make_response(response, 202)

    @staticmethod
    def forbidden(message):
        response = jsonify({
            'message': message
        })
        return make_response(response, 403)

    @staticmethod
    def bad_request(message):
        response = jsonify({
            'message': message
        })
        return make_response(response, 400)

    @staticmethod
    def unauthorized(message):
        response = jsonify({
            'message': message
        })
        return make_response(response, 401)

    @staticmethod
    def success(response):
        return make_response(jsonify(response), 200)
