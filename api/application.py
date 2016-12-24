from flask import Flask, Blueprint
from api.handlers.v1_0.auth_handler import auth_handler
from api.handlers.v1_0.accounts_handler import account_handler
from api.handlers.v1_0.user_handler import user_handler
from api.handlers.v1_0.nerd_handler import nerd_handler
from api.controllers.assets_controller import assets_controller
from api.controllers.view_controller import view_controller
from api.handlers.v1_0.applications_handler import application_handler

bp = Blueprint(__name__, __name__)
app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(bp)
    app.register_blueprint(auth_handler)
    app.register_blueprint(account_handler)
    app.register_blueprint(user_handler)
    app.register_blueprint(nerd_handler)
    app.register_blueprint(application_handler)
    app.register_blueprint(assets_controller)
    app.register_blueprint(view_controller)
    app.run(debug=True, port=9080)