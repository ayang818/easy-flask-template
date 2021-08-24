class Role(object):
    vistor = 1 # 游客，无登录态
    user   = 2 # 用户
    manager= 3 # 管理员

class RoleBuilder(object):

    def __init__(self):
        self.role = []
    
    def append_vistor(self):
        self.role.append(Role.vistor)
        return self
    
    def append_user(self):
        self.role.append(Role.user)
        return self

    def append_manager(self):
        self.role.append(Role.manager)
        return self
    
    def build(self):
        return self.role

    @classmethod
    def all(cls):
        return [Role.vistor, Role.user, Role.manager]

if __name__ == '__main__':
    print(Role.manager)
    print(Role.user)
    print(Role.vistor)