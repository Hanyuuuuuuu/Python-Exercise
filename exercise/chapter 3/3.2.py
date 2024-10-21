"""3-4 嘉宾名单 创建一个列表，至少包含三个你想要邀请的人，并打印邀请消息"""
print("3-4答案：")

names_form = ["aaa", "bbb", "ccc", "ddd"]
for i in range(len(names_form)):
    print(f"\t{names_form[i].title()}你好，今晚有时间吗，我想邀请你一起聚餐!")
print("\n")

for i in names_form:
    print(f"\t{i.title()}你好，今晚有时间吗，我想邀请你一起聚餐!")
print("\n")

for i in names_form:
    print(i)

"""3-5 修改嘉宾名单 一位嘉宾无法赴约，邀请另一位嘉宾"""
# 1、以3-4为基础，程序末尾打印哪位嘉宾无法赴约
# 2、修改嘉宾名单，新嘉宾替换无法赴约的嘉宾
# 3、再次打印消息邀请名单中的嘉宾
print("3-5答案：")

names_form_out = "ccc"
names_form.insert(names_form.index("ccc"), "eee")
names_form.remove(names_form_out)
for i in names_form:
    print(f"\t{i.title()}你好，今晚有时间吗，我想邀请你一起聚餐!")

print(f"\n{names_form_out.title()} 因事无法赴约\n")

"""3-6 添加嘉宾 找到一个大餐桌，再邀请三位新嘉宾"""
# 1、以3-4，3-5为基础，在程序末尾打印找到一个大餐桌
# 2、使用insert()将一位新嘉宾添加到开头
# 3、使用insert（）将另一位新嘉宾添加到中间
# 4、使用append（）将最后一位嘉宾添加到末尾
# 5、再次打印消息邀请嘉宾
print("3-6答案：")

names_form.insert(int(len(names_form)/2), "222")
names_form.insert(0, "111")
names_form.append("333")
print("找到一个更大的餐桌")
for i in names_form:
    print(f"\t{i.title()}你好，今晚有时间吗，我想邀请你一起聚餐!")

"""3-7 缩减名单 新餐桌无法到，只能邀请两位嘉宾"""
# 1、以3-6为基础，在末尾打印只能邀请两位嘉宾的消息
# 2、使用pop（）删除名单直至剩余两人。每删除一位嘉宾都打印消息，无法邀请他
# 3、对剩下的两位打印依然邀请的消息
# 4、使用del删除名单中的最后两位，打印空表
print("3-7答案：")

for i in range(len(names_form)):
    if(len(names_form) == 2):
        break
    else:
        names_form_out = names_form.pop(0)
        print(f"\t{names_form_out.title()}您好，非常抱歉今晚无法邀请您共进晚餐！\n")


for i in range(len(names_form)):
    print(f"\t{names_form[i].title()}你好，今晚有时间吗，我依然想邀请你一起聚餐!")

for i in range(len(names_form)):
    del names_form[0]
print(names_form)

print("非常抱歉，今晚只能邀请两位嘉宾参加聚餐！")
