"""
    列表  list
"""
# 1. 创建
# -- 创建空列表
list01 = []
list02 = list()
# --
list01 = [100,"悟空",True]
# list(可迭代对象)
list02 = list("我是齐天大圣")

# 2. 添加
# -- 追加
list01.append("八戒")
# -- 插入
list01.insert(1,"唐僧")
print(list01)
# 3. 修改
# 将唐三藏地址，赋值给列表第二个元素
list01[1] = "唐三藏"
# 遍历[10,20]，将每个元素赋值给切片位置的元素
list01[-2:] = [10,20]
list01[-2:] = "ok"
print(list01)

# 4. 删除
# -- 根据元素移除
list01.remove("唐三藏")
# -- 根据索引/切片删除
del list01[0]
del list01[-2:]
print(list01)

# 5. 查询
# 索引
print(list02[-1])
# 切片
print(list02[:5])
# 循环
for item in list02:
    print(item)











