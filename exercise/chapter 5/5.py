"""5-1 条件测试 编写一系列条件测试，打印每个测试结果的预测和实际结果"""
# 1、创建测试，分别包含Ture和False结果
print("5-1 答案：")

nums = 123
print("Is nums == 123? I predict Ture.")
print(nums == 123)

print("Is nums == abc? I predict False.")
print(nums == "abc", "\n")

"""5-3 外星人颜色 假设在游戏中射杀了一个外星人，请创建一个名为alien_color的变量，并赋值green，yellow，red"""
# 1、编写一条if语句，检查外星人是否是绿色，如果是，指出玩家获得5分
# 2、编写另一个版本，测试未通过
print("5-3答案：")

alien_color = ["green", "yellow", "red"]
alien = "green"
if alien == "green":
    print("恭喜击杀绿色外星人，获得5分！")

if alien == "yellow":
    print("恭喜击杀黄色外星人，获得10分！\n")

"""5-4 外星人颜色2 编写一个if-else结构 """
# 1、如果外星人是绿色， 打印玩家获得5分
# 2、如果不是绿色，打印玩家获得10分
# 3、编写两个版本，一个执行if语句，一个执行else语句
print("5-4答案：")

if alien == "green":
    print("恭喜击杀绿色外星人获得5分！\n")
alien1 = "yellow"
if alien1 != "green":
    print("恭喜击杀其他颜色外星人获得10分！\n")

if alien == "green":
    print("恭喜击杀绿色外星人获得5分！\n")
else:
    print("恭喜击杀其他颜色外星人获得10分！\n")

"""5-5 外星人颜色3 编写一个if-elif-else结构 """
# 1、如果外星人是绿色， 打印玩家获得5分
# 2、如果是黄色，打印玩家获得10分
# 3、如果是红色，打印玩家获得15分
# 4、分别在三个颜色时打印一条消息
print("5-5答案：")

aliens = ["green", "yellow", "red"]
for alien in aliens:
    if alien == "green":
        print("恭喜击杀绿色外星人获得5分！\n")
    elif alien == "yellow":
        print("恭喜击杀黄色外星人获得10分！\n")
    else:
        print("恭喜击杀红色外星人获得15分！\n")

"""5-6 人生的不同阶段 设置变量age的值，再编写if-elif-else结构，判断处于哪个阶段"""
# 小于2岁，婴儿；2-4，幼儿；4-13，儿童；13-20，青少年；20-65，成年人；大于65，老年
print("5-6答案：")

age = 77
if age < 2:
    print("你是一个婴儿！\n")
elif age < 4:
    print("你是一个幼儿！\n")
elif age < 13:
    print("你是一个儿童！\n")
elif age < 20:
    print("你是一个青少年！\n")
elif age < 65:
    print("你是一个成年人！\n")
else:
    print("你是一个老年人！\n")

"""5-7 喜欢的水果 创建一个水果列表，编写独立的if语句检查列表中是否包含特定的水果"""
# 1、列表命名favorite_fruits
# 编写5条if语句检查，如果是打印消息 You really like banana
print("5-7答案：")

favorite_fruits = ["aaa", "bbb", "ccc"]
a = "aaa"
if a in favorite_fruits:
    print(f"You really like {a}")
d = "ddd"
if d in favorite_fruits:
    print(f"You really like {d}")
b = "bbb"
if b in favorite_fruits:
    print(f"You really like {b}")
e = "eee"
if e in favorite_fruits:
    print(f"You really like {e}")
c = "ccc"
if c in favorite_fruits:
    print(f"You really like {c}")

"""5-8 以特殊方式跟管理员打招呼 创建一个至少包含五个用户的列表，其中一个用户为admin，遍历列表打印问候语"""
# 1、如果用户名为admin，打印特殊问候语hello admin，world you like to see a status report?
# 2、否则，打印普通的问候消息，hello jaden，thank you for logging in again。
print("5-8答案：")

users = ["admin", "aaa", "bbb", "ccc", "ddd"]
for user in users:
    if user == "admin":
        print(f"Hello {user.title()}，world you like to see a status report.")
    else:
        print(f"Hello {user.title()}，thank you for logging in again.")

"""5-9 处理没有用户的情况 在5-8中添加一条if语句，检查用户名为空"""
# 1、如果为空，打印消息We need to find some users！
# 2、删除列表中的所有元素，打印消息
print("5-9答案：")

# for i in range(len(users)):
#     del users[0]

users.clear()

if users:
    print(users)
else:
    print("We need to find some users！")

"""5-10 检查用户名 模拟网站用户名独一无二"""
# 1、创建至少包含5个用户名的列表，命名current_users
# 2、在创建一个包含5个用户名的列表，命名new_users,比包含两个之前的用户
# 3、遍历新列表，检查用户名是否被使用，是，提示需要输入别的用户名，否，提示未被使用
# 4、不区分大小写（可以创建一个current_users的副本，包含全部小写版本
print("5-10答案：")
current_users = ["aaAa", "Bbbb", "cCcc", "ddd", "eee"]
new_users =["AAA", "Bbbb", "FHGF", "HGukhj", "cCcc"]

current_users_lower = current_users[:]
for i in range(len(current_users_lower)):
    current_users_lower[i] = current_users_lower[i].lower()

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("用户名重复，请输入别的用户名！")
    else:
        print("当前用户名未被使用！")

"""5-11 序数 序数表示位置，如1st、2nd和3rd，序数大多以th结尾，只有1、2、3除外"""
# 1、在一个列表中储存数字1-9
# 2、遍历这个列表
# 3、在循环中使用if-elif-else结构，打印每个数字对应的序数
print("5-11答案：")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in nums:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}st")