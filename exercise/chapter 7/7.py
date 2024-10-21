"""7-1 汽车租凭 编写一个程序询问用户要租什么样的汽车，并打印"""
print("7-1 答案：")

# word = "我们的汽车类型有大众，奥迪，特拉斯，本田."
# word += "\n请输入要租的汽车类型： "
# cars = input(word)
# print(f"租的汽车种类是：{cars}")

"""7-2 餐馆定位， 询问有多少人用餐，超过8位，提示没有空桌，否则指出有空桌"""
print("\n7-2 答案：")

# mans = input("请输入用餐人数： ")
# mans = int(mans)

# if mans > 8:
#     print("暂时没有空桌，请稍等。")
# else:
#     print("有空余位置，欢迎用餐。")

"""7-3 10的整数倍 用户输入一个数，指出该数是否是10的整数倍"""
print("\n7-3 答案：")

# num = input("请输入一个数以判断该数是否是10的整数倍： ")
# num = int(num)
#
# if num % 10 == 0:
#     print(f"{num}是10的整数倍。")
# else:
#     print(f"{num}不是10的整数倍。")

"""7-4 比萨配料 编写一个循环，提示用户输入一系列披萨配料，并在用户输入quit时结束循环"""
print("\n7-4 答案：")

# message = ""

# while message != "quit":
#     message = "我们披萨的配料有aaa, bbb, ccc, ddd"
#     message += "\n请填写一种比萨配料, 填写结束请输入quit： "
#     message = input(message)
#     if message != "quit":
#         print(f"您成功添加配料{message}")
#     else:
#         print("您已成功退出配料添加。")

"""7-5 电影票 不到三岁免费，3-12岁12元，超过12岁15元，请编写一个程序询问用户年龄并指出其票价"""
print("\n7-5 答案：")

# active = True
#
# while active:
#     age = input("请输入年龄,结束查询请按q： ")
#     if age == "q":
#         # active = False
#         break
#     else:
#         age = int(age)
#
#         if age < 3:
#             print("票价免费")
#         elif age < 12:
#             print("票价12")
#         elif age >= 12:
#             print("票价15")

"""7-6 以不同的方式完成7-4或7-5"""
print("\n7-6 答案：")

# while True:
#     message = "我们披萨的配料有aaa, bbb, ccc, ddd"
#     message += "\n请填写一种比萨配料, 填写结束请输入quit： "
#     message = input(message)
#     if message != "quit":
#         print(f"您成功添加配料{message}")
#     else:
#         break

"""7-7 无限循环 编写一个无限循环 """
print("\n7-7 答案：")

# num = 0
# while True:
#     num += 1
#     print(num)

"""
7-8 熟食店 创建一个sandwich_orders的列表，在其中包含各种三明治的名字，创建一个空列表名为finished_sandwiches存放制作好的三明治。
遍历第一个列表，打印消息 I made your tuna sandwich，并将其移到第二个列表中，所有三明治都制作好后，打印制作好的三明治列表。
"""
print("\n7-8 答案：")

sandwich_orders = ["aaa", "bbb", "ccc", "ddd"]
finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop(0)
    print(f"I made your {sandwich_order} sandwich")
    finished_sandwiches.append(sandwich_order)

for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)

"""7-9 使用7-8列表，保证其中一个元素出现三次以上,使用while循环将该元素全部删除，打印删除后的列表"""
print("\n7-9 答案：")

finished_sandwiches.append("eee")
finished_sandwiches.insert(0, "eee")
finished_sandwiches.insert(3, "eee")
print(finished_sandwiches)

while "eee" in finished_sandwiches:
    finished_sandwiches.remove("eee")

print(finished_sandwiches)

"""7-10 编写一个程序，调查用户梦想的度假胜地，使用提示If you could visit one place in the world，where would you go？，打印调查结果"""
print("\n7-10 答案：")

diaochas = {}

# 标志
active = True

while active:
    name = input("\nwhat is you name? ")
    diaocha = input("If you could visit one place in the world，where would you go? ")

    # 将name，diaocha储存到字典中
    diaochas[name] = diaocha

    repeat = input("还有人参加调查吗？y/n ")
    if repeat == 'n':
        active = False
print("\n调查结果：")
for name, diaocha in diaochas.items():
    print(f"{name}梦想的旅游圣地是{diaocha}")

