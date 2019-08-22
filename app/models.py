"""__author__= 雍新有"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel():
    # 基础模型
    create_time = db.Column(db.DateTime, default=datetime.now())
    operate_time = db.Column(db.DateTime, default=datetime.now(),
                             onupdate=datetime.now())

    def save(self):
        # 创建和修改
        db.session.add(self)
        db.session.commit()

    def delete(self):
        # 删除
        db.session.delete(self)
        db.session.commit()


class User(BaseModel, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    icon = db.Column(db.String(100), nullable=True)

    __tablename__ = 'user'


# 文章模型
class Article(BaseModel, db.Model):
    # 文章模型
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    body = db.Column(db.Text, nullable=False)
    # index为True - 为这列创建索引，提高查询效率
    # utcnow拿到的是0时区时间 -- 完8小时，我们是东八区。
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    keywords = db.Column(db.String(50), nullable=False)
    c_name = db.Column(db.String(20), db.ForeignKey('category.c_name'), nullable=True)

    __tablename__ = 'article'


class Category(BaseModel, db.Model):
    id = db.Column(db.Integer)
    c_name = db.Column(db.String(20), primary_key=True, unique=True, nullable=False)
    nickname = db.Column(db.String(50), unique=True, nullable=False)
    keywords = db.Column(db.String(50), nullable=False)
    texts = db.relationship('Article', backref='c')

    __tablename = 'category'