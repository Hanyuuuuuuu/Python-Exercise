"""一个用于表示餐馆的类"""


class Restaurant:
    """餐馆的营业信息"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """打印餐馆信息"""
        print(f"餐馆名称为： {self.restaurant_name}")
        print(f"餐馆的类型为： {self.cuisine_type}\n")

    def open_restaurant(self):
        """餐馆是否营业"""
        print(f"{self.restaurant_name}正在营业")

    def number(self):
        """打印就餐人数"""
        print(f"餐馆有{self.number_served}人就餐")

    def set_number_served(self, number):
        """将就餐人数设置为指定的值"""
        """禁止就餐人数回调"""
        if number >= self.number_served:
            self.number_served = number
        else:
            print("就餐人数禁止回调！")

    def increment_number_served(self, number):
        """设置就餐人数递增"""
        """禁止递增人数为负数"""
        if number >= 0:
            self.number_served += number
        else:
            print("禁止增量为负数！")
