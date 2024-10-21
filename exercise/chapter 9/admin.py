"""一个用于表示管理管的类"""
from user import User


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
