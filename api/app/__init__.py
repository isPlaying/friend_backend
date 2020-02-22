from flask import Flask
from app.friend.friend import friend
from dao import db


def register_blueprints(app):
    app.register_blueprint(friend, url_prefix='/friend')


flask_app = Flask(__name__)


def create_app():
    db.init_db()
    register_blueprints(flask_app)
    return flask_app
