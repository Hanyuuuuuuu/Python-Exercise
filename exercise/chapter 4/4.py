"""4-3 数到20 使用for循环打印数1-20（）含"""
print("4-3答案：")
# for i in range(1, 21):
#     print(i)
"""4-4 一百万 创建一个1-1000000的列表，再使用for循环打印出来"""
print("4-4答案：")
form = list(range(1, 1000001))
# for i in form:
#     print(i)
"""4-5 一百万求和 使用min（）和max（）核实列表是从1开始、到1000000结束，使用sunm（）函数求和，看需要多长时间"""
print("4-5答案：")
print(min(form), max(form), sum(form))
"""4-6 奇数 通过函数range（）指定第三个参数，for循环打印1-20的奇数"""
print("4-6答案：")
print("1-20的奇数为：")
for i in range(1, 20, 2):
    print(i)
"""4-7 3的倍数 创建一个列表，其中包含3-30能被3整除的数，for循环打印"""
print("4-7答案：")
nums = []
for i in range(3, 31):
    if i % 3 == 0:
        nums.append(i)
for num in nums:
    print(num)
"""4-8 立方 创建一个列表，包含前10（1-10）个整数的立方，for循环打印"""
print("4-8答案：")
nums = []
for i in range(1, 11):
    i = i ** 3
    nums.append(i)
for num in nums:
    print(num)
"""4-9 立方解析 使用列表解析生成一个列表，包含前10个整数的立方"""
print("4-9答案：")
nums = [num ** 3 for num in range(1, 11)]
print(nums)

"""4-10 切片 选择一个程序，在末尾添加代码完成以下任务"""
# 1、打印消息"The first three items in the list are："，使用切片打印列表的前三个元素
# 2、打印消息"Three items from the middle of the list are："，使用切片打印列表的中间三个元素
# 3、打印消息"The last three items in the list are："，使用切片打印列表的后三个元素
print("4-10答案：")
print("The first three items in the list are：", nums[:3])
print("Three items from the middle of the list are：", nums[4:7])
print("The last three items in the list are：", nums[-3:])

"""4-11 创建一个披萨列表，在创建副本，并赋给变量friend_pizzas完成以下任务"""
# 1、在原来的副本中添加一种披萨
# 2、在副本列表中添加一种披萨
# 3、for循环打印两个列表核实
print("4-11答案：")
pizzas = ["aaa", "bbb", "ccc"]
friend_pizzas = pizzas[:]
pizzas.append("ddd")
friend_pizzas.append("eee")
print("my pizzas:")
for i in pizzas:
    print(i)
print("my friend pizzas:")
for i in friend_pizzas:
    print(i)
"""4-12 使用多个循环 选择一个版本的foods.py，在其中编写两个for循环打印各个食品列表"""
print("4-12答案：")
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
print("my favorite foods are:")
for food in my_foods:
    print(food)

print("my friend's favorite foods are:")
for food in friend_foods:
    print(food)

"""4-13 自助餐 自助餐馆只提供五种简单菜品，请创建元组储存食品"""
# 1、使用for循环打印五种菜品
# 2、尝试修改其中一个元素，python拒绝
# 3、调整菜单，替换其中两种食品。给元组变量赋值，并用for循环打印
print("4-13 答案：")
foods = ("pizza", "duck", "appal", "chicken", "pig")
for food in foods:
    print(food)

# foods[0] = "fish"

foods = ("fish", "duck", "appal", "chicken", "mushroom")
print("替换后菜单为：")
for food in foods:
    print(food)
