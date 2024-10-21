"""3-8 放眼世界 想出至少5个想去旅游的地方 """
# 1、将这些地方储存在一个列表中，并确保不是按字母顺序排列
# 2、按原始顺序打印该表
# 3、使用sorted（）按字母顺序打印该表
# 4、再次打印，核实顺序未变
# 5、使用sorted（）按字母顺序相反打印该表
# 6、再次打印，核实顺序未变
# 7、使用reverse（）修改列表元素顺序，打印核实
# 8、使用reverse（）再次修改排列顺序，核实恢复原始顺序
# 9、使用sort（）修改该列表，使其按字母顺序排序，打印核实
# 10、使用sort（）修改列表，使其按字母顺序相反排序，打印核实
print("3-8答案：")

pleases = ["shanghai", "beijing", "suzhou", "hangzhou", "chongqing", "guizhou"]
print("打印原始列表：")
print(pleases)
print("使用sorted（）按字母顺序打印该表：")
print(sorted(pleases))
print("再次打印，核实顺序未变：")
print(pleases)
print("使用sorted（）按字母顺序相反打印该表：")
print(sorted(pleases, reverse=True))
print("再次打印，核实顺序未变：")
print(pleases)
print("使用reverse（）修改列表元素顺序，打印核实：")
pleases.reverse()
print(pleases)
print("使用reverse（）再次修改排列顺序，核实恢复原始顺序：")
pleases.reverse()
print(pleases)
print("使用sort（）修改该列表，使其按字母顺序排序，打印核实：")
pleases.sort()
print(pleases)
print("使用sort（）修改列表，使其按字母顺序相反排序，打印核实：")
pleases.sort(reverse=True)
print(pleases, "\n")

"""3-8 晚餐嘉宾 使用len（）打印一条消息"""
print("3-8答案：")
print(len(pleases), "\n")

"""3-9 尝试使用各个函数 新建一个列表，使用本章函数处理列表"""
print("3-9答案：")
pleases = ["shanghai", "beijing", "suzhou", "hangzhou", "chongqing", "guizhou"]
print("打印原始列表：\n", pleases)
print("输出列表中的倒数第二个元素并首字母大写：\n", pleases[-2].title())
pleases[0] = "linyi"
print("修改列表第一个值为linyi：\n", pleases)
pleases.append("shanghai")
print("在列表末尾添加元素shanghai：\n", pleases)
pleases.insert(1, "shenyang")
print("在列表第二位插入元素shenyang：\n", pleases)
del pleases[-1]
print("del删除列表最后一个元素shanghai：\n", pleases)
pleases_pop = pleases.pop(2)
print("pop删除列表第三个元素beijing：\n", pleases)
pleases_remove = pleases.remove("linyi")
print("根据值删除元素linyi：\n", pleases)
pleases.sort()
print("使用sort（）方法对列表按字母排序：\n", pleases)
print("使用sorted对列表临时倒序排序：\n", sorted(pleases, reverse=True))
pleases.reverse()
print("使用reverse（）倒着打印列表：\n", pleases)
print("确定列表长度：\n", len(pleases))

