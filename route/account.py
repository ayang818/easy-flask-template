from common.util import SolarException
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
        return "success"

class ModifyUserInfoRoute(BasicRoute):
    methods = ['POST']

    def rule_name(self):
        return 'modify_user_info'

    def process(self):
        pass