"""
    列表推导式
"""
# 需求：在列表中找出所有奇数
list01 = [45, 5, 65, 76, 87, 9]
# list02 = []
# for item in list01:
#     if item % 2 != 0:
#         list02.append(item)
list02 = [item for item in list01 if item % 2 != 0]

# 需求：将list01中所有元素的平方，存入list02
# list02 = []
# for item in list01:
#         list02.append(item ** 2)


list02 = [item ** 2 for item in list01]
print(list02)
