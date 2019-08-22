"""__author__= 雍新有"""
import redis


class Config():
    """
    flask项目的配置信息
    """
    # 数据库的配置
    # mysql+pymysql://root:password@host:port/1902flask
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@47.100.164.252:3306/blog2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'ASDASD123456'

    # 设置session
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.Redis(host='47.100.164.252',
                                port=6379,
                                password='1qaz2wsx')