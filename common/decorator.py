from common.session import PfSessionInfoFactory
from common.role import Role
import functools
from common.embeded import CacheFactory
from flask import request
import logging
from common.const import PF_SESSION_ID
import json
from common.util import SolarException, build_result

# 需要鉴权的接口，process中需要加上 set_authorization 装饰器
def set_authorization(roles):
    """
    对于需要健全的接口，在 Route 类里面重写 roles() 方法 
    """
    def wrapper(func):
        @functools.wraps(func)
        def inner_wrapper(**kwargs):
            # 执行前检测权限
            cookies_dict = request.cookies
            # pf_session_id 会在登录的时候通过 set_cookie 种进页面
            pf_session_id = cookies_dict.get(PF_SESSION_ID)
            pf_session_info = None
            if not pf_session_id:
                # 默认设置 vistor 权限
                pf_session_info = PfSessionInfoFactory.get_pf_session_base_struct()
                pf_session_info['role'] = Role.vistor
            else:
                pf_session_info = CacheFactory.get_cache().get(pf_session_id)
            logging.info("roles=%s",  roles)
            if pf_session_info.get('role') not in roles:
                result = '[authentication denied]please contact pf_manager_mail: chengyi0818@foxmail.com'
            else:
                # 实际执行
                result = func(**kwargs)
            return result
        return inner_wrapper
    return wrapper


def autowire_param(func):
    """
    1. 对于 get 和 post请求，自动将 json 字段 or post 字段打平到 调用函数的参数中
    2. 统一包装response body（包括全局的异常处理）
    """
    @functools.wraps(func)
    def wrapper():
        try:
            if request.method == 'GET':
                args = request.args
                kwargs = {}
                for arg in args:
                    kwargs[arg] = args.get(arg)
                logging.info("req kwargs=%s", kwargs)
                result = build_result(func(**kwargs))
            elif request.method == "POST":
                body = request.get_data()
                kwargs = json.loads(body)
                logging.info("req=%s", kwargs)
                result = build_result(func(**kwargs))
            else:
                result = build_result(body=None, exception=SolarException(code=405, msg='method not allowed'))
        except SolarException as e:
            result = build_result(body=None, exception=e)
        except:
            result = build_result(body=None, exception=SolarException(msg='error'))
        logging.info("resp=%s", result)
        return result
    return wrapper