from flask import Flask, Blueprint, render_template, send_from_directory
from api.handlers.v1_0.auth_handler import auth_handler
from api.handlers.v1_0.accounts_handler import account_handler
from api.handlers.v1_0.user_handler import user_handler
from api.handlers.v1_0.bot_handler import bot_handler

bp = Blueprint(__name__, __name__)
app = Flask(__name__)


@bp.route('/')
def index():
    return render_template('/src/index.html')


@bp.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('templates', path)


@bp.route('/<path:path>')
def send_html(path):
    return send_from_directory('templates/src', path)

if __name__ == '__main__':

    app.register_blueprint(bp)
    app.register_blueprint(auth_handler)
    app.register_blueprint(account_handler)
    app.register_blueprint(user_handler)
    app.register_blueprint(bot_handler)
    app.run(debug=True, port=9082)