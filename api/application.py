from flask import Flask, Blueprint
from api.handlers.v1_0.accounts_handler import account_handler

bp = Blueprint(__name__, __name__)
app = Flask(__name__)


@bp.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':

    app.register_blueprint(bp)
    app.register_blueprint(account_handler)
    app.run(debug=True, port=9080)