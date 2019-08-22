"""__author__= 雍新有"""
from flask_wtf import FlaskForm
from werkzeug.security import check_password_hash
from wtforms import StringField, FileField
from wtforms.validators import DataRequired, Length, EqualTo, \
    Email, ValidationError

from app.models import User, Category, Article


class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired(message='账号必填'),
                                       Length(5, 10, message='账号不能短于5字符,不能长于10字符')])
    password = StringField(validators=[DataRequired(message='密码必填'),
                                       Length(5, 10, message='账号不能短于5字符,不能长于10字符')])

    def validate_username(self, field):
        username = self.data.get('username')
        user = User.query.filter(User.username == username).first()
        if not user:
            raise ValidationError('账号有误')

    def validate_password(self, field):
        username = self.data.get('username')
        password = self.data.get('password')
        user = User.query.filter(User.username == username).first()
        if user:
            if not check_password_hash(user.password, password):
                raise ValidationError('密码错误')


class RegisterForm(FlaskForm):
    username = StringField(validators=[DataRequired(message='账号必填'),
                                       Length(5, 10, message='账号不能短于5字符,不能长于10字符')])
    password = StringField(validators=[DataRequired(message='密码必填'),
                                       Length(5, 10, message='账号不能短于5字符,不能长于10字符')])
    password2 = StringField(validators=[DataRequired(message='确认密码必填'),
                                        EqualTo('password', message='密码和错误密码不一致')])
    email = StringField(validators=[DataRequired(message='邮箱必填'), Email(message='邮箱格式错误')])
    icon = FileField()

    def validate_username(self, field):
        username = field.data
        user = User.query.filter(User.username == username).first()
        if user:
            # 账号已存在
            raise ValidationError('账号已存在！')


class CategoryForm(FlaskForm):
    name = StringField(validators=[DataRequired(message='栏目名必填'),
                                   Length(2, 10, message='栏目名不合规则')])
    nickname = StringField(validators=[DataRequired(message='栏目名必填'),
                                   Length(2, 10, message='栏目名不合规则')])
    keywords = StringField(validators=[DataRequired()])

    def validate_username(self, field):
        c_name = field.data
        category = Category.query.filter(Category.c_name == c_name).first()
        if category:
            # 栏目名已存在
            raise ValidationError('栏目名已存在！')


class ArticleForm(FlaskForm):
    title = StringField(validators=[DataRequired(message='标题必填'),
                                    Length(2, 20, message='标题不合规则')])
    body = StringField(validators=[DataRequired(message='内容必填')])

    keywords = StringField(validators=[DataRequired(message='关键字必填')])

    desc = StringField(validators=[DataRequired(message='描述必填')])

    category = StringField(validators=[DataRequired(message='所属栏目不能为空')])

    def validate_username(self, field):
        title = field.data
        article = Article.query.filter(Article.title == title).first()
        if article:
            # 栏目名已存在
            raise ValidationError('栏目名已存在！')

