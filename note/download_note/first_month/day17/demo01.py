"""
    yield
    练习:exercise01
"""
class MyRange:
    """
        可迭代对象
    """
    def __init__(self, stop):
        self.__stop = stop

    # 程序执行过程：
    #    调用不执行
    #    调用__next__才执行
    #    到yield暂时离开
    #    再次调用__next__继续执行
    #    ...
    # 程序执行原理： "你看见的代码，实际不是这个样子"
    #    将yield关键字以前的代码定义到next方法中
    #    将yield关键字以后的数据作为next方法返回值
    # def __iter__(self):
    #     print("准备数据")
    #     yield 0
    #
    #     print("准备数据")
    #     yield 1
    #
    #     print("准备数据")
    #     yield 2
    #
    #     print("准备数据")
    #     yield 3
    #
    #     print("准备数据")
    #     yield 4

    def __iter__(self):
        begin = 0
        while begin < self.__stop:
            yield begin# 暂时离开，再次调用继续执行
            begin += 1

mr = MyRange(10)
iterator = mr.__iter__()
while True:
    try:
        # 2. 获取下一个元素
        item = iterator.__next__()
        print(item)
    # 3. 如果没有元素则结束循环
    except StopIteration:
        break



# for item in MyRange(5):
#     print(item)  # 0 1 2 3 4

# 循环一次  计算一个  返回一个
# for item in MyRange(99999999999999999999999999999999999999999):
#     print(item)

