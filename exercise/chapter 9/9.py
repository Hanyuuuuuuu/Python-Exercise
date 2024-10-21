"""
9-1 创建一个名为Restaurant的类，其方法__init__()设置属性restaurant_name和cuisine_type。
创建一个describe_restaurant打印前述两项信息和open_restaurant()的方法打印一条消息，指出餐馆正在营业
"""


print("9-1答案：")


class Restaurant:
    """餐馆的营业信息"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印餐馆信息"""
        print(f"餐馆名称为： {self.restaurant_name}")
        print(f"餐馆的类型为： {self.cuisine_type}\n")

    def open_restaurant(self):
        """餐馆是否营业"""
        print(f"{self.restaurant_name}正在营业")


# 创建实列
restaurant = Restaurant("aaa餐厅", "中餐馆")
print(restaurant.restaurant_name, restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

"""9-2 以9-1为基础，创建三个实例，并对每个实例调用方法describe_restaurant()"""
print("\n9-2答案：")

restaurant1 = Restaurant("aaa", "中餐厅")
restaurant2 = Restaurant("bbb", "西餐厅")
restaurant3 = Restaurant("ccc", "卤菜")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

"""9-3 创建User类，包含属性first_name和last_name，以及一些其他属性。describe_user()方法打印用户信息摘要，greet_user()，打印问候"""
print("\n9-3答案：")


class User:
    """这是一个用户信息类"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"用户的姓名为：{self.first_name.title()}{self.last_name}，\n年龄为{self.age}")

    def greet_user(self):
        print(f"{self.first_name.title()}{self.last_name}您好！\n")


user1 = User('han', 'yu', 25)
user2 = User('aaa', 'bbb', 18)

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

"""9-4 以9-1为基础，添加一个number_served的属性，其默认值设置为0，根据这个类创建一个名为restaurant的实例，打印有多人就餐，修改后再次打印"""
# 添加一个set_number_served()方法，能够设置就餐人数。调用这个方法向它传递一个值并打印
# 添加一个increment_number_served()方法，让就餐人数递增，调用方法，向它传递你认为这家餐馆每天可能接待的人数。
print("\n9-4答案：")

# class Restaurant:
#     """餐馆的营业信息"""
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         """打印餐馆信息"""
#         print(f"餐馆名称为： {self.restaurant_name}")
#         print(f"餐馆的类型为： {self.cuisine_type}\n")
#
#     def open_restaurant(self):
#         """餐馆是否营业"""
#         print(f"{self.restaurant_name}正在营业")
#
#     def number(self):
#         """打印就餐人数"""
#         print(f"餐馆有{self.number_served}人就餐")
#
#     def set_number_served(self, number):
#         """将就餐人数设置为指定的值"""
#         """禁止就餐人数回调"""
#         if number >= self.number_served:
#             self.number_served = number
#         else:
#             print("就餐人数禁止回调！")
#
#     def increment_number_served(self, number):
#         """设置就餐人数递增"""
#         """禁止递增人数为负数"""
#         if number >= 0:
#             self.number_served += number
#         else:
#             print("禁止增量为负数！")


# restaurant = Restaurant("aaa", "中餐")
# restaurant.describe_restaurant()
# restaurant.number_served = 10
# restaurant.number()
# restaurant.set_number_served(9)
# restaurant.number()
# restaurant.increment_number_served(-9)
# restaurant.number()

"""9-5 以9-3为基础，添加login_attempts属性，编写increment_login_attempts()方法，将新属性+1，再编写reset_login_attempts(),将属性重置0"""
# 根据User创建一个实例，先调用increment方法多次，保证正确递增，再调用方法reset，确认重置为0
print("\n9-5答案：")

# class User:
#     """这是一个用户信息类"""
#
#     def __init__(self, first_name, last_name, age, login_attempts):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.login_attempts = login_attempts
#
#     def describe_user(self):
#         print(f"用户的姓名为：{self.first_name.title()}{self.last_name}，\n年龄为{self.age}")
#
#     def greet_user(self):
#         print(f"{self.first_name.title()}{self.last_name}您好！\n")
#
#     def increment_login_attempts(self):
#         """login_attempts值加一"""
#         self.login_attempts += 1
#         print(self.login_attempts)
#
#     def reset_login_attempts(self):
#         """login_attempts重置为0"""
#         self.login_attempts = 0
#         print(self.login_attempts)


# user = User("han", "yu", 25, 0)
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.reset_login_attempts()

"""9-6 以9-4为基础，编写一个IceCreamStand的类，继承Restaurant类，添加一个flavors的属性，用于储存冰激凌列表，编写显示方法，创建实例并调用"""
print("\n9-6答案：")


class IceCreamStand(Restaurant):
    """冰激凌小店"""

    # 方法__init__接受创建Restaurant实例所需的信息
    def __init__(self, restaurant_name, cuisine_type, flavors):
        """初始化父类属性"""
        # 调用Restaurant类的方法__init__
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_ice_flavors(self):
        """打印各种口味的冰激凌列表"""
        print(self.flavors)


ice = IceCreamStand("ice", "冰激凌店", ["巧克力味", "香草味", "蓝莓味", "草莓味"])
ice.show_ice_flavors()
ice.open_restaurant()

"""9-7 以9-5为基础，编写Admin类，继承User。添加privileges属性储存字符串列表。编写show_privileges方法，显示管理员权限"""
print("\n9-7答案：")

# class Privileges:
#     """privileges类"""
#
#     def __init__(self, privileges=None):
#         if privileges is None:
#             privileges = ["can add post", "can delete post", "can ban user"]
#         self.privileges = privileges
#         # self.privileges = ["can add post", "can delete post", "can ban user"]
#
#     def show_privileges(self):
#         """打印管理员权限"""
#         print(f"管理员的权限列表如下： {self.privileges}")
#
#
# class Admin(User):
#     """管理员类，继承User"""
#
#     def __init__(self, first_name, last_name, age, login_attempts):
#         """初始化父类属性"""
#         super().__init__(first_name, last_name, age, login_attempts)
#         # 创建一个Privileges实例作为属性
#         self.privileges = Privileges()

# def show_privileges(self):
#     print(f"管理员的权限列表如下： {self.privileges}")


# admin1 = Admin("han", "yu", 25, 0)
# admin1.describe_user()
# admin1.greet_user()
# admin1 = Admin("han", "yu", 25, 0, ["can add post", "can delete post", "can ban user"])


"""9-8 编写一个Privileges类，只有一个privileges属性，储存9-7中的字符串列表，将方法show_privileges转移到这个类中，作为Admin的属性"""
print("\n9-8答案：")

# admin1 = Admin("han", "yu", 25, 0)
# admin1.describe_user()
# admin1.privileges.show_privileges()

"""9-9 在electric_car.py版本中，给Battery类添加一个update_battery的方法，检查电瓶容量，如果不是100，就将其设置为100.创建一辆电瓶
容量为默认值的电动汽车，调用方法get_range，然后对电瓶进行升级，并再次调用方法get_range。将看到电动汽车的续航里程增加"""
print("\n9-9答案：")


class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车属性的值"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = f"{self.year}{self.make}{self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, milege):
        """将里程表读数设置为指定的值"""
        """禁止将里程数回调"""
        if milege >= self.odometer_reading:
            self.odometer_reading = milege
        else:
            print("禁止里程数回调！")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        if miles >= self.odometer_reading:
            self.odometer_reading += miles
        else:
            print("禁止增加里程为负量")


class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类属性"""
        """再初始化电动汽车特有属性"""
        super().__init__(make, model, year)
        # self.battery_size = 75
        self.battery = Battery()
    # def describe_battery(self):
    #     """打印一条描述电瓶容量的消息"""
    #     print(f"This car has a {self.battery_size}-kwh battery.")


class Battery:
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=75):
        """初始化电瓶属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航历程"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """检查电瓶容量"""
        if self.battery_size != 100:
            self.battery_size = 100


car = ElectricCar('audi', 'a4', '2019')
car.battery.get_range()
car.battery.upgrade_battery()
car.battery.get_range()

"""9-10 将最新的Restaurant类储存在一个模块中，在另一个文件中导入Restaurant类，创建一个实例并调用其中一个方法"""
print("\n9-10答案：")

from restaurant import Restaurant

res = Restaurant("aaa", "中餐馆")
res.describe_restaurant()

"""9-11 以9-8为基础，将User类，Privileges类和Admin类储存在一个模块中，在另一个文件中创建Admin实例并调用方法show_privileges。"""
print("\n9-11答案：")

from user import User, Privileges, Admin

user1 = Admin("aaa", "bbb", 22, 0)
user1.privileges.show_privileges()

"""9-12 将User类储存在一个模块中，Privileges类和Admin类储存在另一个模块中，在另一个文件中创建Admin实例并调用方法show_privileges。"""
print("\n9-12答案：")

from admin import Admin

user2 = Admin("han", "yu", 25, 2)
user2.privileges.show_privileges()

"""9-13 创建一个Die类，包含sides属性，默认值6。编写一个roll_die方法，打印1和骰子面数之间的随机数。创建一个六面的骰子再掷10次。"""
# 创建一个10面和20面的骰子，再分别掷10次
print("\n9-13答案：")

from random import randint
import random


class Die:
    """模拟掷骰子"""

    def __init__(self, nums, sides=6):
        self.sides = sides
        self.nums = nums

    def rool_die(self):
        """打印随机投掷数字"""
        for num in range(self.nums):
            # print(randint(1, self.sides))
            print(random.randint(1, self.sides))


die1 = Die(10)
die1.rool_die()
print("\n")
die1 = Die(10, 10)
die1.rool_die()
print("\n")
die1 = Die(10, 20)
die1.rool_die()

"""9-14 创建一个元组或列表，其中包含10个数字和5个字母。从列表中随机选择四个数或字母，并打印一条消息，指出彩票上是这四个数和字母就中奖了。"""
"""9-15 打印消息，报告执行多少次循环才中奖"""
print("\n9-14答案：")

import random

form = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
print("中奖号码：198d")
win_nums = [1, 9, 8, 'd']
loop_num = 0
# print(first_up)
while True:
    loop_num += 1
    first_up = random.choice(form)
    second_up = random.choice(form)
    third_up = random.choice(form)
    fourth_up = random.choice(form)

    if first_up == win_nums[0] and second_up == win_nums[1] and third_up == win_nums[2] and fourth_up == win_nums[3]:
        print(f"您的号码是{first_up}{second_up}{third_up}{fourth_up},恭喜中奖")
        print(f"循环{loop_num}中奖")
        break
    else:
        print(f"您的号码是{first_up}{second_up}{third_up}{fourth_up},很遗憾，您没有中奖")



