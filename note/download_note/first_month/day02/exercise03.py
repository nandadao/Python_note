"""
    根据内存图，写出代码
    变量交换
    11:22
"""
data01 = "孙悟空"
data02 = "猪八戒"
# 变量交换通用思想
# # 1
temp = data01
# 2
data01 = data02
# 3
data02 = temp
# python变量交换
data01, data02 = data02, data01
print(data01)
print(data02)
