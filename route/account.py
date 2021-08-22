from route.base import BasicRoute


class LoginRoute(BasicRoute):
    methods = ['GET']

    def rule_name(self):
        return 'login'

    def process(self):
        return 'login'

class CraeteAccountRoute(BasicRoute):
    methods = ['POST']

    def rule_name(self):
        return 'create_account'

    def process(self):
        pass

class ModifyUserInfoRoute(BasicRoute):
    methods = ['POST']

    def rule_name(self):
        return 'modify_user_info'

    def process(self):
        pass