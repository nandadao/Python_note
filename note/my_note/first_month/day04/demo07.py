"""
    列表
"""
# 1、创建
#   创建空列表
list01 = []
list02 = list()
# ---
list01 = [100, 200]
# print(list03)
#
list02 = list("我是齐天大圣")
# print(list04)

# 2.添加
list01.append("八戒")
print(list01)
#  插入
list01.insert(1, "唐僧")
print(list01)

# 3.修改
list01[1] = "唐三藏"
print(list01)

list01[-2:] = range(10)
print(list01)

# 4.删除
# 根据元素移除
list01.remove("唐三藏")
# 根据索引/切片删除
del list01[0]
print(list01)
del list01[-2:]
print(list01)

# 5、查询
#









