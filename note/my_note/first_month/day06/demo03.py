""""""
"""
    字典推导式
"""

# 需求：range(1, 11 ) key:1--10 value :键的平方
# dict01 = {item: item**2 for item in range(1, 11)}
# print(dict01)


# 需求：range(1, 11 ) key:1--10 value :键的平方
# 需求2.奇数拿出来
# dict01 = {item : item**2 for item in range(1, 11) if item%10 != 0}
# print(dict01)

# 练习1.将一个列表，转换为一个字典
# ["张无忌","赵敏","小昭"]
# {"张无忌":3,"赵敏":2,"小昭":2}
list01 = ["张无忌","赵敏","小昭"]
dict02 = {item:len(item)     for item in list01}
print(dict02)

# 练习2：将两个列表转换为一个字典
# 人名：["张无忌","赵敏","小昭"]
# 房间号：[101, 102, 103]
list01 = ["张无忌","赵敏","小昭"]
list02 = [101, 102, 103]
#  核心思想是：如何同时获取第一个值
dict02 = {list01[i]:list02[i]    for i in range(len(list01))}
print(dict02)

# 练习3.将字典key与value互换
# 价值：互换后，再根据键赵值等同于互换前的根据值找键
#      但是，如果值相同，互换后会丢失数据
dict03 = {v:k    for k,v in dict02.items()}
print(dict03)







