"""
    可迭代对象
"""
list01 = [4, 4, 54, 56, 76]
# 迭代
for item in list01:
    print(item)

# 笔试题：
# 可以被for的条件：
#  对象具有__iter__()方法

# for循环原理
# 1. 获取迭代器
iterator = list01.__iter__()
while True:
    try:
        # 2. 获取下一个元素
        item = iterator.__next__()
        print(item)
    # 3. 如果没有元素则结束循环
    except StopIteration:
        break




