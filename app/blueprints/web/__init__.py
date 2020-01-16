from flask import Blueprint

web = Blueprint('web', __name__)

#注册视图函数
from app.blueprints.web import hello