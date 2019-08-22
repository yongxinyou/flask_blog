"""__author__= 雍新有"""
import os
import uuid

from werkzeug.security import generate_password_hash, check_password_hash

from app.forms import RegisterForm, LoginForm, CategoryForm, ArticleForm
from app.models import User, Category, Article
from utils.functions import login_required
from utils.setting import UPLOAD_DIR

from flask import Blueprint, render_template, redirect, \
    request, url_for, session, jsonify

back = Blueprint('back', __name__)


@back.route('/index/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'GET':
        return render_template('back/index.html')


@back.route('/article/', methods=['GET'])
@login_required
def article():
    if request.method == 'GET':

        articles = Article.query.all()
        return render_template('back/article.html',
                               articles=articles)


@back.route('/add_article/', methods=['GET', 'POST'])
@login_required
def add_article():
    form = ArticleForm()

    if request.method == 'GET':
        return render_template('back/add-article.html',
                               form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            # 通过验证就建文章对象
            article = Article()
            article.title = form.data.get('title')
            article.body = form.data.get('body')
            article.desc = form.data.get('desc')
            article.keywords = form.data.get('keywords')
            article.c_name = form.data.get('category')
            # TODO: 如果栏目不存在，就调转到添加页面
            article.save()
            return redirect(url_for('back.article'))
        errors = form.errors
        return render_template('back/add-article.html',
                               errors=errors,
                               form=form)


@back.route('/article/<int:id>/', methods=['GET', 'POST', 'DELETE'])
@login_required
def article_change(id):
    form = ArticleForm()

    if request.method == 'GET':
        article = Article.query.filter(Article.id == id).first()
        return render_template('back/article-change.html',
                               article=article,
                               form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            article = Article.query.filter(Article.id == id).first()
            article.title = form.data.get('title')
            article.body = form.data.get('body')
            article.desc = form.data.get('desc')
            article.keywords = form.data.get('keywords')
            article.c_name = form.data.get('category')
            # TODO: 如果栏目不存在，就调转到添加页面
            article.save()
            articles = Article.query.all()
            return render_template('back/article',
                                   articles=articles,
                                   message='删除成功')
        errors = form.errors
        return render_template('back/article-change.html',
                               errors=errors,
                               form=form)

    if request.method == 'DELETE':
        # 实现文章栏目
        article = Article.query.filter(Article.id == id).first()
        article.delete()
        # categorys = Category.query.all()
        data = {'code': 200, 'msg': '删除成功'}
        return jsonify(data)


@back.route('/category/', methods=['GET', 'POST'])
@login_required
def category():
    form = CategoryForm()

    if request.method == 'GET':
        categorys = Category.query.all()
        return render_template('back/category.html',
                               categorys=categorys,
                               form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            category = Category()
            category.c_name = form.data.get('name')
            category.nickname = form.data.get('nickname')
            category.keywords = form.data.get('keywords')
            category.save()
            categorys = Category.query.all()
            return render_template('back/category.html',
                                   message='添加成功',
                                   categorys=categorys,
                                   form=form)
        # errors = form.errors
        categorys = Category.query.all()
        return render_template('back/category.html',
                               message='添加有误',
                               categorys=categorys,
                               form=form)


@back.route('/category/<int:id>/', methods=['GET', 'POST', 'DELETE'])
@login_required
def category_change(id):
    form = CategoryForm()

    if request.method == 'GET':
        # 获取对象，渲染页面
        category = Category.query.filter(Category.id == id).first()
        return render_template('back/category2.html',
                               category2=category,
                               form=form)
    if request.method == 'POST':
        # 修改数据
        if form.validate_on_submit():
            category = Category.query.filter(Category.id == id).first()
            category.c_name = form.data.get('name')
            category.nickname = form.data.get('nickname')
            category.keywords = form.data.get('keywords')
            category.save()
            categorys = Category.query.all()
            return render_template('back/category.html',
                                   categorys=categorys,
                                   message='修改成功',
                                   form=form)
        # errors = form.errors
        return render_template('back/category2.html',
                               message='添加有误',
                               form=form)

    if request.method == 'DELETE':
        # 实现删除栏目
        category = Category.query.filter(Category.id == id).first()
        category.delete()
        # categorys = Category.query.all()
        data = {'code': 200, 'msg': '删除成功'}
        return jsonify(data)


@back.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('back/login.html', form=form)

    if request.method == 'POST':
        if form.validate_on_submit():
            # TODO:我还想传递数据给重定向的页面
            session['username'] = form.data.get('username')
            return redirect(url_for('back.index'))
        errors = form.errors
        return render_template('back/login.html',
                               errors=errors,
                               form=form)

#
# @back.route('/logout/', methods=['GET', 'POST'])
# def logout():
#     if request.method == 'POST':
#         session.clear()
#         return redirect(url_for('back.login'))


@back.route('/register/', methods=['GET', 'POST'])
def register():
    # csrf源于form表单，所以先验证form表单，get请求才会生成csrf
    form = RegisterForm()

    if request.method == 'GET':
        return render_template('back/register.html', form=form)

    if request.method == 'POST':
        # 注册
        if form.validate_on_submit():
            user = User()
            user.username = form.data.get('username')
            user.password = generate_password_hash(form.data.get('password'))
            user.email = form.data.get('email')
            if form.data.get('icon'):
                # 保存头像，七牛云，图片服务器，存在项目中
                icon = form.data.get('icon')
                # 自定义文件名，uuid+文件类型
                filename = uuid.uuid4().hex + '.' + icon.mimetype.split('/')[1]
                # 原文件名称
                # filename = icon.filename
                print(os.path.join(UPLOAD_DIR, filename))
                icon.save(os.path.join(UPLOAD_DIR, filename))
                # 数据库存相对路径
                user.icon = os.path.join('images', filename)
            user.save()
            return redirect(url_for('back.login'))
            # 校验失败
        errors = form.errors
        return render_template('back/register.html',
                               errors=errors,
                               form=form)
