import os
import importlib
import logging
from common.decorator import set_authorization
from common.role import Role

# 所有的 Route 必须以 Route 结尾，不然扫描不出来
def register_routes(app):
    # scan test
    # basic_route = BasicRoute()
    # app.add_url_rule(rule=basic_route.name, view_func=basic_route.process)
    routedir_path = os.path.join(os.path.realpath(__file__), '..')
    for file in os.listdir(routedir_path):
        # 如果是个python文件，就import成一个module
        if '.py' not in str(file):
            continue
        # 干掉 python 后缀，file名为 xxx.py
        module = importlib.import_module('route.%s' % (file[:-3]))
        for klass, value in module.__dict__.items():
            if str(klass).endswith('Route'):
                # 向flask添加路由
                route_instance = value()
                # 获取 Route 的路由
                rule_name = route_instance.rule_name()
                if not str(rule_name).startswith('/'):
                    rule_name = '/' + rule_name
                method_list = getattr(route_instance, 'methods', ['GET'])
                try:
                    # TODO 后续如果要给 process 加上默认拓展，在这里添加全局装饰器即可
                    if getattr(route_instance, 'roles', None):
                        route_instance.process = set_authorization(roles=route_instance.roles())(route_instance.process)
                    else:
                        route_instance.process = set_authorization()(route_instance.process)
                    app.add_url_rule(rule=rule_name, view_func=route_instance.process, endpoint=klass, methods=method_list)
                    logging.info("注册成功 %s", klass)
                except AssertionError as e:
                    # 可能是载入了重复的 Route，直接pass即可
                    pass
                except:
                    logging.error("服务注册失败，请检查代码")
                    exit(0)

class BasicRoute(object):
    methods = ['GET']

    def rule_name(self):
        return "/"
    
    def process(self):
        return "pong"

    def roles(self):
        return Role.all()


if __name__=='__main__':
    print(os.path.realpath(__file__))