"""__author__= 雍新有"""

# 登陆状态校验装饰器
# 如果用户登陆了，则可以继续访问被装饰器装饰的函数
# 如果用户没有等了，则不可以访问被装饰器装饰的函数


# 1. 外层函数嵌套内层函数
# 2. 外层函数返回内层函数
# 3. 内层函数要使用外层函数传递的参数
#
# 调用函数，如果带括号，那么是调用函数运行后的结果，
# 调用函数不带括号，调用的是函数本身
from functools import wraps

from flask import session, redirect, url_for


# TODO:1.返回函数func()如何接受参数？
# TODO:2.@wraps(func)的作用？


def login_required(func):
    @wraps(func)
    def check(*args, **kwargs):
        # 步骤1:先从cookie中取出uuid值
        # 步骤2：从redis中字符串类型，key为uuid
        username = session.get('username')
        if not username:
            # 没登录
            return redirect(url_for('back.login'))
        return func(*args, **kwargs)

    return check