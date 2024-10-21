"""8-1 消息 编写一个display_message（）函数，用它打印一个句子，指出你在本章学了什么。"""
print("8-1 答案：")


def display_message():
    print("在本章学习了函数的调用，向函数传递信息，形参和实参")


display_message()

"""8-2 喜欢的图书 编写一个favorite_bbo()的函数，包含名为title的形参，用函数打印一条消息"""
print("\n8-2 答案：")


def favorite_bood(title):
    print(f"最喜欢的书是{title.title()}。")


favorite_bood("python编程")

"""8-3 创建一个函数，包括尺码和印刷字样两个参数，使用位置实参和关键字实参分别打印一个句子"""
print("\n8-3 答案：")


def make_shirt(size="xl", word="I love Python"):
    print(f"T恤的尺码是{size}, 需要印刷的字体是{word}")


# 位置实参
make_shirt("m", "hello")
# 关键字实参
make_shirt(word="hay", size="l")

"""8-4 修改make_shirt()，默认情况下制作I love python的大号T恤，调用函数制作一件默认字样大号，一件默认字样中号，一件其他字样T恤"""
print("\n8-4 答案：")
# 默认字大号
make_shirt()
# 默认字中号
make_shirt("m")
# 其他
make_shirt("s", "I love Java")

"""8-5 编写一个describe_city()的函数，包括城市名字和国家两个参数，给国家的形参一个默认值，调用三次函数，至少一个国家不属于默认值"""
print("\n8-5 答案：")


def describe_city(city, guojian="中国"):
    print(f"{city} is in {guojian}")


describe_city("上海")
describe_city(city="苏州")
describe_city(guojian="日本", city="东京")

"""8-6 编写一个city_country()的函数，包括城市名称及其所属国家，返回格式类似字符串”Santiago，Chile“，至少使用三个城市"""
print("\n8-6 答案：")


# 使用返回值
def city_country(city, country):
    word = f'"{city.title()},{country.title()}"'
    return word


shanhai = city_country("shanghai", "china")
print(shanhai)
linyi = city_country("linyi", "china")
print(linyi)
suzhou = city_country("suzhou", "china")
print(suzhou)

"""
8-7 编写一个make_album()的函数，它创建一个描述音乐的字典。函数包括歌手的名字和专辑，返回一个包含着两项信息的字典，使用函数创建三个字典。
给函数添加一个默认值为None的可选形参，储存歌曲数
"""
print("\n8-7 答案：")


def make_album(name, misc, num=None):
    """返回专辑字典"""
    if num:
        miscs = {"name": name.title(), "misc": misc, "num": num}
    else:
        miscs = {"name": name.title(), "misc": misc}
    return miscs


miscs1 = make_album("周深", "深的深")
print(miscs1)
miscs2 = make_album("檀健次", "一专")
print(miscs2)
miscs3 = make_album("aaa", "bbb", 123)
print(miscs3)

"""8-8 在8-7的基础上编写一个while循环，让用户输入专辑的歌手和名称，获取信息后调用函数打印字典，务必提供退出途径"""
print("\n8-8 答案：")

# while True:
#     print("请输入专辑的歌手名和专辑名")
#     print("退出请按q")
#
#     name = input("请输入歌手名： ")
#     if name == 'q':
#         break
#
#     misc = input("请输入专辑名： ")
#     if misc == 'q':
#         break
#
#     misc4 = make_album(name, misc)
#     print("\n", misc4)

"""8-9 创建一个列表，包含一系列文本信息，将该列表传递给show_messages()函数，打印每条文本信息"""
print("\n8-9 答案：")


def show_messages(texts):
    """循环打印列表信息"""
    print("列表的信息为：")
    for text in texts:
        print(text)


texts = ['aaaaaaaaa', 'bbbbbbb', 'cccccccccc']
show_messages(texts)

"""8-10 在8-9基础上，编写一个send_message()的函数，将每条消息打印出来，并移到一个sent_message的列表中，打印两个列表"""
print("\n8-10 答案：")


def send_message(texts, sent_message):
    """移动列表元素"""
    while texts:
        text = texts.pop()
        print(f"正在移动文本信息{text}")
        sent_message.append(text)


sent_message = []
# send_message(texts, sent_message)

# show_messages(texts)
# show_messages(sent_message)

"""8-11 在8-10基础上，编写一个sent_message列表的副本，向函数传递副本，打印两个列表"""
print("\n8-11 答案：")

texts1 = texts[:]

send_message(texts1, sent_message)

show_messages(texts)
show_messages(sent_message)

"""8-12 编写一个函数，只有一个形参，接受顾客在三明治中添加的一系列食材。调用函数三次，每次提供不同数量的实参"""
print("\n8-12 答案：")


def sanmingzhi(*shicai):
    print("三明治中添加的食材包括：")
    print(shicai)


sanmingzhi("番茄")
sanmingzhi("番茄", "芝士")
sanmingzhi("番茄", "芝士", "洋葱")

"""8-13 复制程序user_profile.py,在其中调用build_profile()创建简介"""
print("\n8-13 答案：")


def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["lasr_name"] = last
    return user_info


user_profile = build_profile("han", "yu",
                             xingbie="女",
                             age=25,
                             birsday=1998)
print(user_profile)

"""8-14 编写一个函数，将一辆汽车的信息储存在字典中。这个函数接受制造商和型号和任意数量的关键字实参"""
print("\n8-14 答案：")


def make_car(make, type, **car_info):
    car_info["make"] = make
    car_info["type"] = type
    return car_info


car = make_car("aaa", "bbb", color="blue", tow_package=True)
print(car)

"""8-15 将示例printing_models.py中的函数放在一个名为printing_functions.py的文件中，在printing_models的开头编写一条import语句"""
print("\n8-15 答案：")

import printing_functions

unprinted_designs = ['prone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)

"""8-16 在主程序文件中，使用多种方法导入函数，再调用"""
print("\n8-16 答案：")

import printing_functions
from printing_functions import print_models, show_completed_models
from printing_functions import print_models as pm
import printing_functions as pf
from printing_functions import *

