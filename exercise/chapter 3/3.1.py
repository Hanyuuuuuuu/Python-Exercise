"""3-1 姓名 将一些朋友的姓名储存在一个列表中，并将其命名为names，依次访问该列表中的每个元素，从而将每个朋友的姓名打印出来"""
names = ["aaa", "bbb", "ccc", "ddd"]
print(names[0])
print(names[1].title())
print(names[-2].title())
print(f"my friend {names[-1].title()} is good\n")

"""
3-2 问候语 继续使用3-1中的列表，但不打印每个朋友的姓名，而为每个人打印一条消息。
每条消息都包含相同的问候语，但抬头为响应朋友的姓名
"""
for i in range(4):
    print(f"{names[i].title()} good morning")

"""3-3 自己的列表 创建一个交通工具列表，并打印相关宣言"""
bools = ["motorcycle", "bus", "car", "cycle"]
print(f"\nI would like to own a Honda motorcycle")
