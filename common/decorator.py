from common.session import PfSessionInfoFactory
from common.role import Role
import functools
from common.embeded import CacheFactory
from flask import request
import logging
from common.const import PF_SESSION_ID

# 需要鉴权的接口，process中需要加上 set_authorization 装饰器
def set_authorization(roles=[Role.user]):
    def wrapper(func):
        @functools.wraps(func)
        def inner_wrapper():
            # 执行前检测权限
            logging.info("request=%s", request.cookies)
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
            if pf_session_info.get('role') not in roles:
                result = '[authentication denied]please contact pf_manager_mail: chengyi0818@foxmail.com'
            else:
                # 实际执行
                result = func()
            return result
        return inner_wrapper
    return wrapper
