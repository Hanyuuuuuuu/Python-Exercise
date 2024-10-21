"""一个用于表示用户的类"""


class User:
    """这是一个用户信息类"""

    def __init__(self, first_name, last_name, age, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"用户的姓名为：{self.first_name.title()}{self.last_name}，\n年龄为{self.age}")

    def greet_user(self):
        print(f"{self.first_name.title()}{self.last_name}您好！\n")

    def increment_login_attempts(self):
        """login_attempts值加一"""
        self.login_attempts += 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        """login_attempts重置为0"""
        self.login_attempts = 0
        print(self.login_attempts)


class Privileges:
    """privileges类"""

    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges
        # self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """打印管理员权限"""
        print(f"管理员的权限列表如下： {self.privileges}")


class Admin(User):
    """管理员类，继承User"""

    def __init__(self, first_name, last_name, age, login_attempts):
        """初始化父类属性"""
        super().__init__(first_name, last_name, age, login_attempts)
        # 创建一个Privileges实例作为属性
        self.privileges = Privileges()