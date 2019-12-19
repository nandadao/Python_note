"""
    元组tuple
    练习:exercise08
"""

# 1. 创建
tuple01 = (4, 54, 5, 6, 7)
list01 = [3, 4, 5, 6]
# 预留空间 --> 按需分配
tuple02 = tuple(list01)
# 按需分配 --> 预留空间
list02 = list(tuple01)
print(list02)
print(tuple02)

# 注意：(元素) -->   元素
#      (元素,) -->  元组
tuple03 = (10,)
print(type(tuple03))

# 2. 查询
tuple04 = ("无忌", "悟空")
name01, name02 = tuple04

# 索引
print(tuple04[0])
# 切片
print(tuple04[:2])
# 循环
for item in tuple04:
    print(item)

for i in range(len(tuple04) - 1, -1, -1):
    print(tuple04[i])
