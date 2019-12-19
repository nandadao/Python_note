"""
    列表内存图
    练习:exercise01

"""
list01 = ["张无忌","张翠山"]
list02 = list01
# 修改的是列表第一个元素
list01[0] = "无忌"
print(list02[0])

list01 = ["张无忌","张翠山"]
list02 = list01
# 修改的是变量list01
list01 = "无忌"
print(list02[0])
