from flask import Flask, Blueprint
from api.handlers.v1_0.auth_handler import auth_handler
from api.handlers.v1_0.accounts_handler import account_handler
from api.handlers.v1_0.user_handler import user_handler

bp = Blueprint(__name__, __name__)
app = Flask(__name__)


@bp.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':

    app.register_blueprint(bp)
    app.register_blueprint(auth_handler)
    app.register_blueprint(account_handler)
    app.register_blueprint(user_handler)
    app.run(debug=True, port=9080)