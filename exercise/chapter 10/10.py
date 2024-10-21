"""10-1 新建一个文本文件。编写一个程序打印文本文件三次：打印整个文件；遍历文件对象；将各行储存在一个列表中，在with代码外打印"""

print("10-1 答案：")

# 打印整个文件
with open('learning_python.txt') as file_object:
    file = file_object.read()
    print(file)

# 打印时遍历文件对象
with open('learning_python.txt') as file_object:
    for file in file_object:
        print(file.rstrip())

print("\n")
# 在with外打印
with open('learning_python.txt') as file_object:
    file_list = file_object.readlines()

for file in file_list:
    print(file.rstrip())

"""10-2 使用方法replace将字符串中的特定单词替换成另一个。用C替换10-1中的python"""
print("\n10-2 答案：")

for file in file_list:
    file_c = file.replace('Python', 'C')
    print(file_c.rstrip())

"""10-3 编写一个程序，提示用户输入名字。用户做出响应后，将名字写入文件guest.txt"""
print("\n10-3 答案：")

# name = input("请输入姓名： ")
#
# with open('guest.txt', 'w') as file_name:
#     file_name.write(name)

"""10-4 编写一个while循环，提示用户输入名字。用户输入名字后打印一条问候语，并将访问记录添加到guest_book.txt中"""
print("\n10-4 答案：")
#
# while True:
#     """循环添加访问记录"""
#     name = input("请输入您的姓名，如停止输入请按q: ")
#     if name != 'q':
#         print(f"{name.title()}欢迎您！")
#         with open('guest_name.txt', 'a') as file_name:
#             file_name.write(f"{name.title()}\n")
#     else:
#         break

"""10-5 编写一个while循环，询问用户为何喜欢编程，当用户输入一个原因之后，都将其添加到一个储存所有原因的文件中"""
print("\n10-5 答案：")

# while True:
#     """循环询问喜欢编程的原因"""
#     resource = input("请问你喜欢编程的原因时什么？,结束询问请按q： ")
#     if resource != 'q':
#         with open('resource.txt', 'a') as file_object:
#             file_object.write(f"{resource}\n")
#     else:
#         break

"""10-6 编写一个加法运算，打印结果。在用户输入非数字时，捕获ValueError异常，并打印一条友好消息"""
print("\n10-6 答案：")

# print("这是一个加法运算，请输入需要进行运算的数字！")
#
# try:
#     num1 = input("请输入第一个加数： ")
#     num1 = int(num1)
#     num2 = input("请输入第二个加数： ")
#     num2 = int(num2)
# except ValueError:
#     pass
#     # print("输入非法数字")
# else:
#     num_sum = num1 + num2
#     print(num_sum)

"""10-7 将10-6的代码放在while循环中，让用户犯错后能够继续输入数"""
print("\n10-7 答案：")

print("这是一个加法运算，请输入需要进行运算的数字！")
print("结束计算请按q。")

# while True:
#     try:
#         num1 = input("请输入第一个加数： ")
#         if num1 != 'q':
#             num1 = int(num1)
#         else:
#             break
#         num2 = input("请输入第二个加数： ")
#         if num2 != 'q':
#             num2 = int(num2)
#         else:
#             break
#     except ValueError:
#         pass
#         # print("输入非法数字")
#     else:
#         num_sum = num1 + num2
#         print(num_sum)

"""10-8 创建cats.txt,dogs.txt，每个文件至少储存三个名字。读取文件并打印到屏幕上，将这些代码放到try-except代码块中，
文件不存在时捕获FileNotFound错误，并显示一条消息"""
print("\n10-8 答案：")

# with open('cats.txt', 'w', encoding='utf-8') as f:
#     f.write("肉肉\n")
#     f.write("包子\n")
#     f.write("aaa\n")
# with open('dogs.txt', 'w', encoding='utf-8') as f:
#     f.write("元宝\n")
#     f.write("妞妞\n")
#     f.write("毛毛\n")


files = ['cats.txt', 'dogs.txt', 'aaa']

try:
    for file in files:
        with open(file, encoding='utf-8') as f:
            print(f.read())
except FileNotFoundError:
    print(f"文件{file}没有发现")

"""10-9 修改10-8，任意文件不在时，静默失败"""
print("\n10-9 答案：")


def count_words(filename):
    """打印文件内容"""

    try:
        with open(filename, encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        pass


files = ['cats.txt', 'dogs.txt', 'aaa']
for file in files:
    count_words(file)

"""10-10 访问古登堡计划，下载作品文件。编写一个程序，使用count（）和lower（）方法计算文件中‘the’在每个作品中出现的次数，
由于‘then’和‘them’也算在内，再计算‘the ’出现的次数"""
print("\n10-10 答案：")

"""10-11 编写一个程序，提示用户输入喜欢的数， 并使用json.dump()将这个数储存到文件中。再编写一个程序，从文件中提前这个值并打印消息"""
print("\n10-11 答案：")
import json

# filename = 'like_num.json'
# num = input("你喜欢的数是什么？ ")
#
# with open(filename, 'w') as f:
#     json.dump(num, f)
#
# with open(filename) as f:
#     file_num = json.load(f)
#     print(f"我知道你喜欢的数是{file_num}")

"""10-12 将10-2中的程序合二为一，如果用户储存了喜欢的数，就向用户显示它，否则提示用户输入喜欢的数，并将其存储到文件中"""
print("\n10-12 答案：")

# filename = 'like_nums.json'
#
# try:
#     with open(filename) as f:
#         file_num = json.load(f)
# except FileNotFoundError:
#     num = input("你喜欢的数是什么？ ")
#     with open(filename, 'w') as f:
#         json.dump(num, f)
#         print(f"你喜欢的数是{num}")
# else:
#     print(f"我知道你喜欢的数是{file_num}")

"""10-13 修改remember_me.py，在greet_user中打印欢迎回来之前，询问用户名是否正确，如果不对，调用get_new_username让用户输入正确的用户名"""
print("\n10-13 答案：")


def get_stored_username():
    """如果储存了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("你的名字是什么？ ")
    filename = 'username.json'
    with open(filename, 'a') as f:
        json.dump(username, f)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        choic = input(f"你的用户名{username}是否正确？请输入y/n。 ")
        if choic.lower() == 'y':
            print(f"{username}欢迎回家！")
        elif choic.lower() == 'n':
            username = get_new_username()
            print(f"{username},当你下次回来的时候我会记住你的名字！")
        else:
            print("输入未识别，请输入y/n。 ")
    else:
        username = get_new_username()
        print(f"{username},当你下次回来的时候我会记住你的名字！")


greet_user()



