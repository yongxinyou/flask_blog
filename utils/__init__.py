"""__author__= 雍新有"""
from flask import Flask
from flask_session import Session

from app.back_views import back
from app.models import db
from app.web_views import web
from utils.config import Config
from utils.setting import STATIC_DIR, TEMPLATE_DIR


def create_app():

    app = Flask(__name__,
                static_folder=STATIC_DIR,
                template_folder=TEMPLATE_DIR)

    # 加载配置文件
    app.config.from_object(Config)
    # 加载蓝图对象
    app.register_blueprint(blueprint=web, url_prefix='/web')
    app.register_blueprint(blueprint=back, url_prefix='/back')

    # 加载第三方sqlachemhy
    db.init_app(app)

    # 加载session
    sess = Session()
    sess.init_app(app)
    return app