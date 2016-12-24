from flask import Blueprint, render_template
from design_config import config

view_controller = Blueprint(__name__, __name__)


@view_controller.route('/login', methods=['GET'])
def authenticate():
    return render_template('index.html')


@view_controller.route('/', methods=['GET'])
def home():
    if config == "prod":
        return render_template('dist/index.html')
    return render_template('src/dev-index.html')