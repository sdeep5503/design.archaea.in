from flask import Blueprint, render_template
from design_config import config

view_controller = Blueprint(__name__, __name__)


@view_controller.route('/login', methods=['GET'])
def authenticate():
    if config == "prod":
        return render_template('dist/authenticate.html', base_url='127.0.0.1:9080')
    return render_template('src/authenticate.html', base_url='127.0.0.1:9080')


@view_controller.route('/', methods=['GET'])
def home():
    if config == "prod":
        return render_template('dist/index.html', base_url='127.0.0.1:9080')
    return render_template('src/dev-index.html', base_url='127.0.0.1:9080')
