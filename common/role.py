class Role(object):
    vistor = 1 # 游客，无登录态
    user   = 2 # 用户
    manager= 3 # 管理员

    @classmethod
    def all(cls):
        return [Role.vistor, Role.user, Role.manager]


if __name__ == '__main__':
    print(Role.manager)
    print(Role.user)
    print(Role.vistor)