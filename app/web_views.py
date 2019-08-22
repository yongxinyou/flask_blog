
from flask import Blueprint, render_template, request

from app.models import Category, Article

web = Blueprint('web', __name__)


@web.route('/index/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        categorys = Category.query.all()
        for category in categorys:
            stus = category.texts
            num = len(stus)
            setattr(category, 'a_num', num)
        # TODO:怎么查id小于5的文章对象
        articles = Article.query.all()
        return render_template('web/index.html',
                               categorys=categorys,
                               articles=articles)

    if request.method == 'POST':
        pass


@web.route('/list/', methods=['GET'])
def list():
    if request.method == 'GET':
        categorys = Category.query.all()
        for category in categorys:
            stus = category.texts
            num = len(stus)
            setattr(category, 'a_num', num)
        articles = Article.query.all()
        return render_template('web/list.html',
                               categorys=categorys,
                               articles=articles)


@web.route('/list/<int:id>/', methods=['GET', 'POST'])
def list_show(id):
    if request.method == 'GET':
        categorys = Category.query.all()
        for category in categorys:
            stus = category.texts
            num = len(stus)
            setattr(category, 'a_num', num)
        category2 = Category.query.filter(Category.id == id).first()
        articles = category2.texts
        return render_template('web/list.html',
                               categorys=categorys,
                               articles=articles)


@web.route('/about/', methods=['GET'])
def about():
    if request.method == 'GET':
        categorys = Category.query.all()
        for category in categorys:
            stus = category.texts
            num = len(stus)
            setattr(category, 'a_num', num)
        return render_template('web/about.html',
                               categorys=categorys)


@web.route('/gbook/', methods=['GET'])
def gbook():
    if request.method == 'GET':
        categorys = Category.query.all()
        for category in categorys:
            stus = category.texts
            num = len(stus)
            setattr(category, 'a_num', num)
        # TODO:怎么查id小于5的文章对象
        articles = Article.query.all()
        return render_template('web/gbook.html',
                               categorys=categorys,
                               articles=articles)


@web.route('/info/', methods=['GET'])
def info():
    if request.method == 'GET':
        categorys = Category.query.all()
        for category in categorys:
            stus = category.texts
            num = len(stus)
            setattr(category, 'a_num', num)
        articles = Article.query.all()
        return render_template('web/info.html',
                               categorys=categorys,
                               articles=articles)


@web.route('/info/<int:id>/', methods=['GET'])
def info_show(id):
    if request.method == 'GET':
        categorys = Category.query.all()
        for category in categorys:
            stus = category.texts
            num = len(stus)
            setattr(category, 'a_num', num)
        articles = Article.query.all()
        article1 = Article.query.filter(Article.id == id).first()
        article2 = Article.query.filter(Article.id == id-1).first()
        article3 = Article.query.filter(Article.id == id+1).first()
        return render_template('web/info.html',
                               categorys=categorys,
                               articles=articles,
                               article1=article1,
                               article2=article2,
                               article3=article3)
