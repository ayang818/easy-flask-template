# coding=utf-8
from flask import Flask
import logging
import os
from route.base import register_routes

def config_logger():
    """
    设置日志等级
    """
    logging.getLogger().setLevel(logging.INFO)

config_logger()

def create_app(config=None):
    """
    创建 bootstrap app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path,'flaskr.sqlite'),
    ) 
    if not config:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(config)
    
    try:
        if not os.path.exists(app.instance_path):
            os.makedirs(app.instance_path)
    except OSError as e:
        logging.error('启动失败 %s', e)
    # 注册路由
    register_routes(app)
    return app

app = create_app()
logging.info("%s", os.path.join(app.instance_path,'flaskr.sqlite'))
app.run(host='localhost', port='5000')
