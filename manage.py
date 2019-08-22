"""__author__= 雍新有"""
from flask_script import Manager

from utils import create_app


# 获取flask对象app
app = create_app()


if __name__ == '__main__':
    manage = Manager(app)
    manage.run()