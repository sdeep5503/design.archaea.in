from flask import Blueprint, send_from_directory

assets_controller = Blueprint(__name__, __name__)


@assets_controller.route('/js/<path:path>', methods=['GET'])
def js(path):
    return send_from_directory('templates', 'src/js/' + path)


@assets_controller.route('/css/<path:path>', methods=['GET'])
def css(path):
    return send_from_directory('templates', 'src/css/' + path)


@assets_controller.route('/dist/<path:path>', methods=['GET'])
def dist(path):
    return send_from_directory('templates', 'dist/' + path)


@assets_controller.route('/<path:path>', methods=['GET'])
def templates(path):
    return send_from_directory('templates', 'src/templates/' + path)


@assets_controller.route('/img/<path:path>', methods=['GET'])
def images(path):
    return send_from_directory('templates', 'src/img/' + path)
