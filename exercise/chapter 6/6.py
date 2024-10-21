"""6-1 人 用字典储存一个人的信息，包括名，姓，年龄和居住的城市，并打印"""
print("6-1 答案：")

man = {"first_name": "han", "last_name": "yu", "age": "25", "city": "shanghai", }
print(man)
print(man["first_name"])
print(man.get("last_name"))
print(man.get("xingbie", "键不存在"))

"""6-2 喜欢的数 创建一个字典包括五个人名作为键，他们喜欢的数作为值，打印每个人的名字和喜欢的数"""
print("\n6-2 答案：")

mens = {
    "aaa": 1,
    "bbb": 2,
    "ccc": 3,
    "ddd": 4,
    "eee": 5,
}
print(mens)

"""\n6-3 6-4词汇表"""
# 1、创建一个词汇表，包括五个编程术语作为键，它们的含义作为值
# 2、以整洁的方式打印每个术语及其含义
# 使用循环遍历字典中的键和值，无误后再添加五个术语
print("\n6-3 6-4答案：")

python = {
    "int": "数据类型为整型",
    "for": "for循环",
    "if": "if判断语句",
    "str": "字符串",
    "float": "浮点数",
}

python["list"] = "列表"
python["set"] = "集合"
python["update"] = "更新"
python["append"] = "添加元素"
python["del"] = "删除"

for key, value in python.items():
    print(f"{key}的含义是：{value}")

"""6-5 河流 创建一个字典，储存三条河流以及流经国家"""
# 1、使用循环为每条河流打印一条消息
# 2、使用循环将该字典中每条河流的名字打印出来
# 3、使用循环将该字典中包含的国家名字打印出来
print("\n6-5 答案：")

helius = {
    "he1": "guojia1",
    "he2": "guojia2",
    "he3": "guojia3",
}
for he, guojia in helius.items():
    print(f"{he}流经{guojia}.")

for he in helius.keys():
    print(he)

for guojia in set(helius.values()):
    print(guojia)

"""6-6 调查 在6.3.1的程序中执行以下操作"""
# 1、创建一个应该会接受调查的人员名单，其中一些人已包含在字典中
# 2、遍历名单，对已参与调查的人表示感谢，未参与的人邀请参加
print("\n6-7 答案：")

names = ['jen', 'sarah', 'edward', 'phil', 'aaa', 'bbb', 'ccc']
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

print("\n")
for name in names:
    if name in favorite_languages.keys():
        print(f"{name}您好，感谢您参与这次调查。")
    else:
        print(f"{name}您好，邀请您参与这次调查。")

"""6-7 创建三个人的字典，然后将三个字典储存在应该pople列表中，遍历列表，打印消息"""
print("\n6-7 答案：")

man1 = {"first_name": "han", "last_name": "yu", "age": "25", "city": "shanghai", }
man2 = {"first_name": "tan", "last_name": "jianci", "age": "30", "city": "guangxi", }
man3 = {"first_name": "zhou", "last_name": "shen", "age": "29", "city": "guizhou", }

poples = [man1, man2, man3]
for pople in poples:
    print(pople)

"""6-8 创建多个宠物字典，包含宠物类型和主人名字，将这些字典储存在一个pets的列表中，遍历列表，打印宠物信息"""
print("\n6-8 答案：")

pet1 = {"name": "rourou", "host_name": "hanyu"}
pet2 = {"name": "baozi", "host_name": "hanxue"}

pets = [pet1, pet2]
for pet in pets:
    print(pet)

"""6-9 喜欢的地方 创建一个favorite_places，包含三个人作为键，每个人喜欢1-3个地方，遍历字典，打印名字和喜欢的地方"""
print("\n6-9 答案：")

favorite_place = {
    "hanyu": ["suzhou", "shenyang"],
    "aaa": ["shangh", "nanjing", "haerbin"],
    "bbb": ["hangzhou", "guangxi"],
}

for key, value in favorite_place.items():
    print(f"{key.title()} like {value}")

"""6-10 喜欢的数 修改6-2，让每个人喜欢多个数，打印人名和喜欢的数"""
print("\n6-10 答案：")

mans = {
    "aaa": [1, 2, 3],
    "bbb": [2, 3, 4],
    "ccc": [3, 4],
    "ddd": [4, 5, 6],
    "eee": [5, 6, 7, 8],
}

for key, value in mans.items():
    print(f"{key.title()} like num are: {value}")

"""6-11 城市 创建一个cities的字典，包含三个城市键，每个城市创建一个字典，包含所属国家、人口以及介绍，打印每个城市及其信息"""
print("\n6-11 答案：")

cities = {
    "shanghai": {"country": "china", "population": "100000", "fact": "aaa"},
    "linyi": {"country": "china", "population": "200000", "fact": "bbb"},
    "shenyang": {"country": "china", "population": "300000", "fact": "ccc"},
}

for key, value in cities.items():
    print(f"{key.title()}相关信息:")
    for k, v in value.items():
        print(f"{k}: {v}")
    print("\n")
