"""
    元组
"""
# 1.创建

tuple01 = (2, 3,4,42,2)
list01 = [2, 4, 6, 2]
# 预留空间  -->  按需分配
tuple02 = tuple(list01)

# 按需分配 --> 预留空间
list01 = list(tuple01)
print(list01)
print(tuple02)

# 注意：(元素)  --> 元素
#      (元素,)  --> 元组
tuple03 = (10,)
print(tuple03)




# 2.查询
tuple04 = ("无忌", "悟空")
name01, name02 = tuple04
# print(name01)
# print(name02)
# # 索引
# print(tuple04[0])
# # 切片
# print(tuple04[:2])
# # 切片会复制

# 循环
for item in tuple04:
    print(item)

for i in range(len(tuple04)-1 , -1 , -1):
    print(tuple04[i])





















