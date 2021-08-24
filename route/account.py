from common.role import RoleBuilder
from common.util import ErrorCode, SolarException
from route.base import BasicRoute
from flask import request
import logging

class LoginRoute(BasicRoute):
    methods = ['GET']

    def rule_name(self):
        return 'login'

    def process(self, username, password):
        logging.info("username=%s, password=%s", username, password)
        return 'login'

class CraeteAccountRoute(BasicRoute):
    methods = ['POST']

    def rule_name(self):
        return 'create_account'

    def process(self, username, password, student_number):
        if username == '1':
            raise SolarException(code=ErrorCode.VALIDATE_EXCEPTION, msg='username can not be 1')
        return "success"

    def roles(self):
        # 只有管理员可以创建账号
        return RoleBuilder().append_manager().build()

class ModifyUserInfoRoute(BasicRoute):
    methods = ['POST']

    def rule_name(self):
        return 'modify_user_info'

    def process(self):
        pass