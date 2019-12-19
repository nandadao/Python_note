"""
    练习:
        自定父MyRange类，实现下列效果(给出一个数，输出01234)
"""


class MyRange:
    def __init__(self, number=0):
        self.__number = number

    # def __iter__(self):
    #     return MyRangeIterator(self.__number)

    # 调用不执行
    # 调用__next__才执行
    # 到yield暂时离开
    # 再次调用__next__ 继续执行
    # ...


    # 程序执行原理：你看见的代码实际不是这个样子
    #   1.将yield关键字以前的代码定义到next方法中
    #   2.将yield关键字以后的数据作为next方法返回值
    def __iter__(self):
        begin = 0
        while begin < self.__number:
            yield begin   # 暂时离开，再次调用继续执行
            begin += 1



# 循环一次，计算一个，返回一个
for item in MyRange(5):
    print(item)  # 0 1 2 3 4

# # for循环原理
# # 1.获取迭代器
# iterator = list01.__iter__()
# while True:
#     try:
#         # 2.获取下一个元素
#         item = iterator.__next__()
#         print(item)
#     # 3.如果没有元素则结束循环
#     except StopIteration:
#         break
























    


    
    


























