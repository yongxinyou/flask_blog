"""__author__= 雍新有"""
import os

# 拿到当前文件的全部路径的上一层的上一层, 就是项目的根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_DIR = os.path.join(BASE_DIR, 'static')

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

UPLOAD_DIR = os.path.join(STATIC_DIR, 'images')