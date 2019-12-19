"""
    可迭代对象
"""
# 面试题
# 可以被for 的条件
# 对象具有__iter__()方法



list01 = [1, 6, 2, 7, 4, 4, 2]

# for循环原理
# 1.获取迭代器
iterator = list01.__iter__()
while True:
    try:
        # 2.获取下一个元素
        item = iterator.__next__()
        print(item)
    # 3.如果没有元素则结束循环
    except StopIteration:
        break






